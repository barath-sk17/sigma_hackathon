import streamlit as st
import pandas as pd

# CSS for styling
st.markdown(
    """
    <style>
    .reportview-container {
        background: #f0f5f5;
    }
    .sidebar .sidebar-content {
        background: #57859c;
    }
    .stMarkdown {
        font-size: 16px !important;
    }
    .st-eb {
        padding-top: 10px;
        padding-bottom: 10px;
    }
    .st {
        margin-top: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def calculate_returns(price_data):
    returns = [(price_data[i] - price_data[i-1]) / price_data[i-1] for i in range(1, len(price_data))]
    return returns

def calculate_state(returns):
    states = []
    a = []
    for ret in returns:
        if ret >= 0.01:
            states.append("Bull")
            a.append(1)
        elif ret > -0.01:
            states.append("Flat")
        else:
            states.append("Bear")
    print(len(a))
    return states

def portfolio_calculator(states):
    new_val = [0]*len(states)
    for i in range(len(states)-1):
        if states[i] == "Flat" and states[i+1] == "Bull":
            new_val[i+1] = new_val[i]+1
        elif states[i] == "Flat" and states[i+1] == "Bear":
            new_val[i+1] = new_val[i]-1
        else:
            new_val[i+1] = new_val[i]
    return new_val[-1]

def calculate_optimal_indices(states,returns):
    store_indices = []
    for i in range(len(states)-1):
        if states[i] == "Bear" and states[i+1] == "Bull":
            store_indices.append(i+1)
        elif states[i] == "Flat" and states[i+1] == "Bull":
            store_indices.append(i+1)
        
        # might consider in certain cases
        
        # elif (states[i] == "Bull" and states[i+1] == "Bull") and (returns[i]<returns[i+1]):
        #    store_indices.append(i+1)
        

    return store_indices

def calculate_transition_distribution(states):
    state_transitions = {'Bear': {'Bear': 0, 'Flat': 0, 'Bull': 0},'Flat': {'Bear': 0, 'Flat': 0, 'Bull': 0}, 'Bull': {'Bear': 0, 'Flat': 0, 'Bull': 0}}
    prev_state = 'Bear'
    
    for state in states:
        state_transitions[prev_state][state] += 1
        prev_state = state
    
    total_transitions = sum(sum(transitions.values()) for transitions in state_transitions.values())
    transition_distribution = {key: {next_state: count / total_transitions for next_state, count in transitions.items()} for key, transitions in state_transitions.items()}
    
    return transition_distribution

def main(price_data):
    returns = calculate_returns(price_data)
    states = calculate_state(returns)
    portfolio_val = portfolio_calculator(states)
    indices = calculate_optimal_indices(states,returns)
    transition_distribution = calculate_transition_distribution(states)
    # Display results using Streamlit
    st.title('Portfolio Analysis')
    st.subheader('Portfolio Value (V(N)):')
    st.markdown(f"<div class='value'>{portfolio_val}</div>", unsafe_allow_html=True)
    st.markdown(f"")
    st.subheader('Optimal Buy Indices:')
    with st.expander("Optimal Buy Indices"):
        df = pd.DataFrame.from_dict(indices)
        st.dataframe(df)
    st.markdown(f"")
    st.markdown(f"<div class='value'>Length : {len(indices)}</div>", unsafe_allow_html=True)
    st.markdown(f"")
    st.subheader('Transition Distribution:')
    # Display transition distribution in a collapsible section
    with st.expander("Transition Distribution"):
        df = pd.DataFrame.from_dict(transition_distribution)
        st.dataframe(df)


# Read dataset
data = pd.read_csv("QuantRocket.csv")  # Replace "your_dataset.csv" with the path to your dataset
price_data = data[data['Field'] == 'Close']['FIBBG000B9XRY4'].tolist()



# Run the Streamlit app
if __name__ == '__main__':
    main(price_data)
