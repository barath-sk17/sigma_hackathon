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
    for ret in returns:
        if ret >= 0.01:
            states.append("Bull")
        elif ret > -0.01:
            states.append("Flat")
        else:
            states.append("Bear")
    return states

def calculate_transition_distribution(states):
    state_transitions = {'Flat': {'Bull': 0, 'Flat': 0, 'Bear': 0}, 'Bull': {'Bull': 0, 'Flat': 0, 'Bear': 0}, 'Bear': {'Bull': 0, 'Flat': 0, 'Bear': 0}}
    prev_state = 'Flat'
    
    for state in states:
        state_transitions[prev_state][state] += 1
        prev_state = state
    
    total_transitions = sum(sum(transitions.values()) for transitions in state_transitions.values())
    transition_distribution = {key: {next_state: count / total_transitions for next_state, count in transitions.items()} for key, transitions in state_transitions.items()}
    
    return transition_distribution

def main(price_data):
    returns = calculate_returns(price_data)
    states = calculate_state(returns)
    transition_distribution = calculate_transition_distribution(states)
    
    V = 0  # Initial portfolio value
    optimal_buy_indices = []  # Store indices where buy orders are placed
    
    for i, state in enumerate(states):
        # Update portfolio value based on rules
        if state == 'Bull' and (i == 0 or states[i - 1] == 'Flat'):
            V += 1
            optimal_buy_indices.append(i)
        elif state == 'Bear' and (i == 0 or states[i - 1] == 'Flat'):
            V -= 1
            optimal_buy_indices.append(i)
    
    # Display results using Streamlit
    st.title('Portfolio Analysis')
    st.subheader('Portfolio Value (V(N)):')
    st.markdown(f"<div class='value'>{V}</div>", unsafe_allow_html=True)
    st.markdown(f"")
    st.subheader('Optimal Buy Indices:')
    with st.expander("Optimal Buy Indices"):
        df = pd.DataFrame.from_dict(optimal_buy_indices)
        st.dataframe(df)
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
