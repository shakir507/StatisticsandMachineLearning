#This code simulates the stochastic Lorenz system
import argparse
import numpy as np
import matplotlib.pyplot as plt
'''
        return np.array(
            [
                params["sigma"] * (y[1] - y[0]),
                y[0] * (params["rho"] - y[2]) - y[1],
                y[0] * y[1] - params["beta"] * y[2],
            ]
        )'''

def initialize_parameters(args):
    params={}
    paramnames=['sigma',  # sigma is the rate of the flow of x
        'rho',      # rho is the rate of the flow of y
        'beta',        # beta is the rate of the flow of z
        'initial_x',
        'initial_y',
        'initial_z'
        ]
    for paramname in paramnames:
        if not hasattr(args, paramname):
            raise ValueError('Parameter {} is missing'.format(paramname))
        else:
            params[paramname]=getattr(args, paramname)
    
    return params

def initialize_state(params):
    state = {
        'x': int(params['initial_x']),
        'y': int(params['initial_y']),
        'z': int(params['initial_z'])
    }
    return state

def calculate_rates(state, params):

    rates = {
        'rate_birth_x': params['sigma'] * state['y'],
        'rate_death_x': params['sigma'] * state['x'],
        'rate_birth_y': params['rho'] * state['x'],
        'rate_death_y': state['x']*state['z']+state['y'],
        'rate_birth_z': state['x']*state['y'],
        'rate_death_z': params['beta']*state['z'],
    }
    return rates

def update_state(state, event_type):
    if event_type == "BirthX":
        state['x'] += 1
    elif event_type == "DeathX":
        state['x'] -= 1
    elif event_type == "BirthY":
        state['y'] += 1
    elif event_type == "DeathY":
        state['y'] -= 1
    elif event_type == "BirthZ":
        state['z'] += 1
    elif event_type == "DeathZ":
        state['z'] -= 1
    return state

def run_simulation(args):
    params = initialize_parameters(args)
    state = initialize_state(params)
    event_types = list(calculate_rates(state, params).keys())
    event_type_mapping = {
    'rate_birth_x': 'BirthX',
    'rate_death_x': 'DeathX',
    'rate_birth_y': 'BirthY',
    'rate_death_y': 'DeathY',
    'rate_birth_z': 'BirthZ',
    'rate_death_z': 'DeathZ',
}

    t = 0
    events = []
    t_max=args.tmax
    while t < t_max:
        rates = calculate_rates(state, params)
        total_rate = sum(rates.values())
        rate_sums = np.cumsum(list(rates.values()))
        # if state['I_h'] == 0 or state['E_h'] == 0:
        #     break
        dt = np.random.exponential(1 / total_rate)
        t += dt
        event_prob = np.random.uniform(0, 1)
        for i, event_type in enumerate(event_types):
            if i == 0 and event_prob < rate_sums[i] / total_rate:
                event_type = "BirthX"
            if i > 1 and i < len(event_types) - 1 and event_prob > rate_sums[i - 1]/total_rate and event_prob < rate_sums[i] / total_rate:
                event_type = event_type_mapping[event_types[i]]
            if i == len(event_types) - 1 and event_prob > rate_sums[i - 1]/total_rate and event_prob < rate_sums[i] / total_rate:
                event_type = "DeathZ"

            state = update_state(state, event_type)
            events.append((t, state['x'], state['y'], state['z'], event_type))
            # print(state['S_v'], state['E_v'], state['I_v'], state['R_v'])
    return events

def plot_results(events):
    # Extract data for plotting
    times = [event[0] for event in events]
    x_values = [event[1] for event in events]
    y_values = [event[2] for event in events]
    z_values = [event[3] for event in events]

    
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # # Plot human variables on the left y-axis
    # ax1.plot(times, x_values, label='X', linestyle='--', color='tab:blue')
    # ax1.plot(times, y_values, label='Y', linestyle='-', color='tab:orange')
    # ax1.plot(times, z_values, label='Z', linestyle='-', color='tab:green')
    ax1.plot(z_values, y_values, label='x-y', linestyle='-', color='tab:red')
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y', color='tab:blue')
    ax1.tick_params(axis='y', labelcolor='tab:blue')


    plt.title('Stochastic Lorenz Model Simulation')
    plt.grid(True)
    plt.savefig('../Data/StochasticLorenz.png')
    # plt.show()


if __name__ == "__main__":
    tmax=500
    parser=argparse.ArgumentParser()
    defaults_vals = {'--tmax': 500,  # Maximum time for simulation
                     '--path': '../Data/',  # Path to save the events
                     '--output_file': 'LorenzEvents.csv',  # Output file name
        '--sigma': 10,  # human death rate
        '--rho': 28,      # disease-induced death rate
        '--beta': 8/3,        # infection rate for humans
        '--initial_x': 1,
        '--initial_y': 1,
        '--initial_z': 1
    }
    defaults_help={'--tmax': 'Maximum time for simulation','--path': 'Path to save the events','--output_file': 'Output file name',
                   '--sigma': 'Lorenz sigma parameter',
                   '--rho': 'Lorenz rho parameter',
                   '--beta': 'Lorenz beta parameter',
                   '--initial_x': 'initial_x',
                   '--initial_y': 'initial_y',
                   '--initial_z': 'initial_z'
                   }
    for key, value in defaults_vals.items():
        parser.add_argument(key, type=type(value), default=value, help=defaults_help[key])

    args=parser.parse_args()
    events=run_simulation(args)
    save_path = '../Data/'
    with open(save_path+'LorenzEvents.csv', 'w') as f:
        for event in events:
            f.write(str(event)+'\n')
    # #load events from file
    # events = []
    # with open(save_path+'SEIR_SEI_events.txt', 'r') as f:
    #     for line in f:
    #         events.append(eval(line))
    plot_results(events)