from aocd import get_data, submit

year, day = 2023, 20

# parse data
data = get_data(year=year, day=day).split("\n")

modules = {}
for line in data:
    left, right = line.split(" -> ")
    module_type = None
    module_name = left
    module_destinations = right.split(", ")
    if left[0] in ["%", "&"]:
        module_type = left[0]
        module_name = left[1:]

    modules[module_name] = {
        "type": module_type,
        "destinations": module_destinations,
        "state": None
    }

# need to module all input models to & module, initially remembering low pulse
for k, v in modules.items():
    if v["type"] != "&":
        continue
    v["state"] = {}
    for k2, v2 in modules.items():
        if k in v2["destinations"]:
            v['state'][k2] = "low"
    modules[k] = v

pulses = []
index = 0

for push_button in range(1, 1000):
    pulses.append({
        "start": "button",
        "signal": "low",
        "end": "broadcaster"
    })
    while index < len(pulses):
        p = pulses[index]
        index += 1

        if p['end'] not in modules.keys():
            continue

        module = modules[p['end']]

        if module["type"] is None:
            new_signal = p['signal']

        elif module["type"] == "%":
            if module["state"] is None:
                module["state"] = "off"
            if p['signal'] == "high":
                continue
            # otherwise must be low
            new_signal = "high" if module["state"] == "off" else "low"
            module["state"] = "on" if module["state"] == "off" else "off"

        elif module["type"] == "&":
            module["state"][p['start']] = p['signal']
            if "low" in module["state"].values():
                new_signal = "high"
            else:
                new_signal = "low"

        else:
            raise Exception("unknown model type")

        modules[p['end']]['state'] = module["state"]
        for dest in module["destinations"]:
            new_pulse = {"start": p['end'], "signal": new_signal, "end": dest}
            pulses.append(new_pulse)

        # required to find 'high' cycle times for 4 inputs into xm
        # if modules["xm"]["state"]["ng"] == "high": # sv, jz, ft
        #     print(push_button)


# part A
low_pulses = len([p for p in pulses if p['signal'] == "low"])
high_pulses = len([p for p in pulses if p['signal'] == "high"])
answer_a = low_pulses * high_pulses
print(answer_a)
# submit(answer_a, part="a", day=day, year=year)

# part B
# find cycles for 4 inputs into xm using the final if statement in loop
# lcm the cycle times
# DONE
# submit(answer_b, part="b", day=day, year=year)