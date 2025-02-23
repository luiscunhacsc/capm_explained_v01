import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Configure the Streamlit app
st.set_page_config(layout="wide")
st.title("📊 Understanding the Capital Asset Pricing Model (CAPM)")
st.markdown("""
Analyze how different parameters affect the expected return of an asset using the CAPM formula:
$$
E(R_i) = R_f + \beta_i (E(R_m) - R_f)
$$
Where:
- $E(R_i)$: Expected return of the asset.
- $R_f$: Risk-free rate.
- $\beta_i$: Beta of the asset.
- $E(R_m)$: Expected market return.
""")

# Sidebar for input parameters
with st.sidebar:
    st.header("⚙️ Parameters")
    
    # Reset button
    def reset_parameters():
        st.session_state["rf_slider"] = 0.02
        st.session_state["rm_slider"] = 0.08
        st.session_state["beta_slider"] = 1.0
    
    st.button("↺ Reset Parameters", on_click=reset_parameters)
    
    rf = st.slider("Risk-Free Rate ($R_f$)", 0.0, 0.1, 0.02, key="rf_slider")
    rm = st.slider("Expected Market Return ($E(R_m)$)", 0.0, 0.2, 0.08, key="rm_slider")
    beta = st.slider("Beta ($\\beta$)", 0.0, 3.0, 1.0, key="beta_slider")
    
    # Disclaimer
    st.markdown("---")
    st.markdown("""
    **⚠️ Disclaimer**  
    *Educational purposes only. No accuracy guarantees. Do not use this tool for financial decisions without consulting a qualified professional.*  
    """)

# CAPM function
def calculate_capm(rf, rm, beta):
    expected_return = rf + beta * (rm - rf)
    return expected_return

# Create tabs for different sections
tab1, tab2, tab3, tab4 = st.tabs([
    "🎮 Interactive Tool", 
    "📚 Theory Behind CAPM", 
    "📖 Comprehensive Tutorial", 
    "🛠️ Practical Labs"
])

# Tab 1: Interactive Tool
with tab1:
    # Calculate CAPM
    expected_return = calculate_capm(rf, rm, beta)
    
    # Display results in columns
    col1, col2 = st.columns([1, 3])
    with col1:
        st.success(f"### Expected Return: **{expected_return:.2%}**")
        st.markdown(f"""
        ### Key Parameters
        - **Risk-Free Rate ($R_f$):** `{rf:.2%}`
        - **Market Return ($E(R_m)$):** `{rm:.2%}`
        - **Beta ($\\beta$):** `{beta:.2f}`
        """)
    
    with col2:
        # Visualize Security Market Line (SML)
        fig, ax = plt.subplots(figsize=(10, 5))
        betas = np.linspace(0, 3, 100)
        returns = rf + betas * (rm - rf)
        
        ax.plot(betas, returns, label="Security Market Line (SML)", color="darkblue", linewidth=2)
        ax.scatter(beta, expected_return, color="red", label=f"Your Asset (β={beta:.2f})", zorder=5)
        ax.axhline(rf, color="gray", linestyle="--", label="Risk-Free Rate")
        ax.set_title("Security Market Line (SML)", fontweight="bold")
        ax.set_xlabel("Beta ($\\beta$)")
        ax.set_ylabel("Expected Return")
        ax.grid(alpha=0.3)
        ax.legend()
        st.pyplot(fig)

# Tab 2: Theory Behind CAPM
with tab2:
    st.markdown("""
    ## Capital Asset Pricing Model (CAPM): Mathematical Foundation
    
    ### Model Overview
    The CAPM is a widely used model to estimate the expected return of an asset based on its systematic risk ($\\beta$). It assumes:
    1. Investors are rational and risk-averse.
    2. Markets are efficient.
    3. A single-period investment horizon.
    4. All investors have access to the same information.
    
    ### Core Equation
    $$
    E(R_i) = R_f + \\beta_i (E(R_m) - R_f)
    $$
    Where:
    - $E(R_i)$: Expected return of the asset.
    - $R_f$: Risk-free rate (e.g., Treasury bond yield).
    - $\\beta_i$: Beta, measuring the asset's sensitivity to market movements.
    - $E(R_m)$: Expected market return.
    
    ### Key Insights
    - **Risk-Free Rate ($R_f$)**: The baseline return for taking no risk.
    - **Market Risk Premium ($E(R_m) - R_f$)**: Compensation for bearing market risk.
    - **Beta ($\\beta$)**: Amplifies or dampens market movements:
      - $\\beta > 1$: Aggressive stocks (more volatile than the market).
      - $\\beta < 1$: Defensive stocks (less volatile than the market).
      - $\\beta = 1$: Moves in line with the market.
    
    ### Limitations
    - Assumes markets are efficient (not always true).
    - Ignores unsystematic risk (diversifiable risk).
    - Relies on historical data for beta estimation.
    """)

# Tab 3: Comprehensive Tutorial
with tab3:
    st.markdown("""
    ## Welcome to the CAPM Learning Tool!
    
    **What this tool does:**  
    This interactive calculator helps you understand how the CAPM formula works and how different parameters affect expected returns. Perfect for learning about risk and return!
    
    ### Quick Start Guide
    
    1. **Adjust Parameters** (Left Sidebar):
       - Move sliders to set risk-free rate, market return, and beta.
    
    2. **View Results** (Main Panel):
       - Real-time expected return calculation.
       - Visualize the Security Market Line (SML).
    
    3. **Try These Examples**:
       - 🎚️ Set $\\beta = 0$: Notice the return equals the risk-free rate.
       - ⚡ Set $\\beta = 2$: See how aggressive stocks amplify returns.
       - 💹 Compare $\\beta = 0.5$ vs $\\beta = 1.5$: Observe sensitivity to market movements.
    
    ### Key Features to Explore
    - **SML Visualization**: Understand how beta affects expected returns.
    - **Real-World Scenarios**: Test different market conditions.
    - **Dynamic Explanations**: Learn about beta, risk premiums, and more.
    
    **Pro Tip:** Use the reset button ↺ to quickly return to default values!
    """)

# Tab 4: Practical Labs
with tab4:
    st.header("🔬 Practical CAPM Labs")
    st.markdown("""
    Welcome to the **Practical CAPM Labs** section! Each lab provides a real-world scenario or demonstration 
    to help you apply the CAPM formula in a hands-on way.
    
    Experiment, take notes, and enjoy exploring how assets behave under different market conditions!
    """)
    
    # Lab choice
    lab_choice = st.radio(
        "Select a lab to view:",
        ("Lab 1: Beta Sensitivity",
         "Lab 2: Market Risk Premium",
         "Lab 3: Portfolio Construction"),
        index=0
    )
    
    if lab_choice == "Lab 1: Beta Sensitivity":
        st.subheader("📊 Lab 1: Understanding Beta Sensitivity")
        st.markdown("""
        **Real-World Scenario:**  
        You're analyzing two stocks: one with $\\beta = 0.5$ (defensive) and another with $\\beta = 2.0$ (aggressive).  
        How do their expected returns change as the market return fluctuates?
        
        **Learning Objective:**  
        - Understand how beta amplifies or dampens market movements.
        - Practice interpreting beta values.
        
        **Suggested Steps**:
        1. Set $R_f = 2\%$, $E(R_m) = 8\%$.
        2. Compare expected returns for $\\beta = 0.5$ and $\\beta = 2.0$.
        3. Increase $E(R_m)$ to 12%. Observe how returns change.
        4. Decrease $E(R_m)$ to 4%. Repeat the analysis.
        """)
    
    elif lab_choice == "Lab 2: Market Risk Premium":
        st.subheader("💹 Lab 2: Market Risk Premium Impact")
        st.markdown("""
        **Real-World Scenario:**  
        In a high-risk environment, the market risk premium ($E(R_m) - R_f$) increases.  
        How does this affect the expected return of assets with different betas?
        
        **Learning Objective:**  
        - Explore the relationship between market risk premium and expected returns.
        - Understand why higher-risk environments favor aggressive stocks.
        
        **Suggested Steps**:
        1. Set $R_f = 2\%$, $E(R_m) = 10\%$.
        2. Compare expected returns for $\\beta = 1.0$ and $\\beta = 1.5$.
        3. Increase $E(R_m)$ to 15%. Observe the impact.
        4. Decrease $E(R_m)$ to 5%. Repeat the analysis.
        """)
    
    else:  # Lab 3: Portfolio Construction
        st.subheader("💼 Lab 3: Portfolio Construction Using CAPM")
        st.markdown("""
        **Real-World Scenario:**  
        You're constructing a portfolio with two assets: one defensive ($\\beta = 0.5$) and one aggressive ($\\beta = 2.0$).  
        How do you allocate weights to achieve a target portfolio beta?
        
        **Learning Objective:**  
        - Learn how to combine assets to achieve desired risk levels.
        - Practice calculating portfolio beta.
        
        **Suggested Steps**:
        1. Set $R_f = 2\%$, $E(R_m) = 8\%$.
        2. Allocate 60% to the defensive asset and 40% to the aggressive asset.
        3. Calculate the portfolio beta:  
           $$
           \\beta_{portfolio} = w_1 \\beta_1 + w_2 \\beta_2
           $$
        4. Adjust weights to achieve a target beta (e.g., $\\beta = 1.0$).
        """)