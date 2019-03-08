import sys
state= {"Rainy", "Sunny"}
observation = {"happy","sad"}
start_probability = {"Rainy":1/3, "Sunny":2/3}
transition_probability = {"Rainy":{'Rainy':0.6, 'Sunny':0.4}, "Sunny":{'Rainy':0.2, 'Sunny':0.8}}
emission_probability = {"Rainy":{'happy':0.4, 'sad':0.6}, "Sunny":{'happy':0.8, 'sad':0.2}}

def main():
    sys_in = sys.argv[1]
    processed_in = []
    for i in sys_in:
        if i != "H" and i != "S":
            raise Exception("input should be a chine like 'HSSHH' with H indicate as happy and S indicates sad")
        if i == "H":
            processed_in.append("happy")
        elif i == "S":
            processed_in.append('sad')
    event_list = []
    start_dir = {}
    for i in state:
        first_prob = start_probability[i] * emission_probability[i][processed_in[0]]
        start_dir[first_prob] = i
    event_list.append([start_dir[max(start_dir.keys())],max(start_dir.keys())])
    for element_num in range(len(processed_in)-1):
        event_list.append(find_max_transi(event_list[element_num], processed_in[element_num+1]))
    output_str = ""
    for event in event_list:
        output_str = output_str + event[0] + " > "
    print(output_str[:-2])
    print("Final Probability is : " + str(event_list[-1][1]))


def find_max_transi(previous_event, current_observation):
    previous_state = previous_event[0]
    previous_prob = previous_event[1]
    current_dir = {}
    for current_state in state:
        current_prob = previous_prob * transition_probability[previous_state][current_state] * emission_probability[current_state][current_observation]
        current_dir[current_prob] = current_state
    return [current_dir[max(current_dir.keys())], max(current_dir.keys())]

main()

