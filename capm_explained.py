import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

#######################################
# 1) Define callback functions:
#    - One to reset defaults
#    - One for each lab's parameters
#######################################
def reset_parameters():
    st.session_state["rf_slider"] = 0.02
    st.session_state["rm_slider"] = 0.08
    st.session_state["beta_slider"] = 1.0

def set_lab1_parameters():
    st.session_state["rf_slider"] = 0.02
    st.session_state["rm_slider"] = 0.08
    st.session_state["beta_slider"] = 1.5

def set_lab2_parameters():
    st.session_state["rf_slider"] = 0.03
    st.session_state["rm_slider"] = 0.12
    st.session_state["beta_slider"] = 2.0

def set_lab3_parameters():
    st.session_state["rf_slider"] = 0.01
    st.session_state["rm_slider"] = 0.05
    st.session_state["beta_slider"] = 0.5

def set_lab4_parameters():
    st.session_state["rf_slider"] = 0.04
    st.session_state["rm_slider"] = 0.10
    st.session_state["beta_slider"] = 0.8

def set_lab5_parameters():
    st.session_state["rf_slider"] = 0.02
    st.session_state["rm_slider"] = 0.06
    st.session_state["beta_slider"] = 1.2

#######################################
# CAPM function
#######################################
def calculate_capm(rf, rm, beta):
    expected_return = rf + beta * (rm - rf)
    return expected_return

#######################################
# Configure the Streamlit app
#######################################
st.set_page_config(layout="wide")
st.title("📊 Understanding the Capital Asset Pricing Model (CAPM)")
st.markdown("""
Analyze how different parameters affect the expected return of an asset using the CAPM formula:
$$
E(R_i) = R_f + \\beta_i (E(R_m) - R_f)
$$
Where:
- $E(R_i)$: Expected return of the asset.
- $R_f$: Risk-free rate.
- $\\beta_i$: Beta of the asset.
- $E(R_m)$: Expected market return.
""")

# Sidebar for input parameters
with st.sidebar:
    st.header("⚙️ Parameters")
    
    # Reset button
    st.button("↺ Reset Parameters", on_click=reset_parameters)
    
    rf = st.slider("Risk-Free Rate ($R_f$)", 0.0, 0.1, 0.02, key="rf_slider")
    rm = st.slider("Expected Market Return ($E(R_m)$)", 0.0, 0.2, 0.08, key="rm_slider")
    beta = st.slider("Beta ($\\beta$)", 0.0, 3.0, 1.0, key="beta_slider")
    
    # Disclaimer and license
    st.markdown("---")
    st.markdown(
        """
        **⚠️ Important Legal Disclaimer**  
        This tool is purely for educational purposes. No accuracy guarantees are provided.  
        The author, **Luís Simões da Cunha**, does not engage in financial advising or endorse any specific investment strategies.  
        All information provided is for illustrative and educational purposes only and should not be construed as financial or investment advice.  
        
        **Key Points:**  
        - The Capital Asset Pricing Model (CAPM) is a theoretical framework and may not reflect real-world market conditions.  
        - Always consult a qualified, accredited financial advisor before making any financial decisions.  
        - Use of this tool implies acceptance of these terms.  

        **License:**  
        This work is licensed under a [Creative Commons Attribution-NonCommercial 4.0 International License](https://creativecommons.org/licenses/by-nc/4.0/).  
        You are free to share and adapt this material for non-commercial purposes, provided you give appropriate credit to the author, **Luís Simões da Cunha**, and indicate if changes were made.  

        ![License Badge](https://licensebuttons.net/l/by-nc/4.0/88x31.png)  
        By Luís Simões da Cunha  
        """,
        unsafe_allow_html=True
    )

# Create tabs for different sections
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🎮 Interactive Tool", 
    "📚 Theory Behind CAPM", 
    "📖 Comprehensive Tutorial", 
    "🛠️ Practical Labs",
    "🧠 The Very Basics of CAPM"
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
    The CAPM helps investors estimate the expected return of an asset based on its systematic risk ($\\beta$). It assumes:
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
    
    Use the **"Set Lab Parameters"** buttons to jump directly to recommended settings for each scenario.
    Experiment, take notes, and enjoy exploring how assets behave under different market conditions!
    """)
    
    # --- Additional Disclaimer ---
    st.warning("""
    **Disclaimer**:  
    This material is purely for educational purposes. Do not use this tool for financial decisions without consulting a qualified professional.
    """)

    # A radio to choose one of the labs
    lab_choice = st.radio(
        "Select a lab to view:",
        ("Lab 1: Beta Sensitivity",
         "Lab 2: Market Risk Premium",
         "Lab 3: Portfolio Construction",
         "Lab 4: Defensive vs Aggressive Stocks",
         "Lab 5: High-Risk Environments"),
        index=0
    )
    
    # ---------------- Lab 1 ----------------
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
        1. Click "**Set Lab 1 Parameters**" to use $R_f = 2\\%$, $E(R_m) = 8\\%$, $\\beta = 1.5$.
        2. Compare expected returns for $\\beta = 0.5$ and $\\beta = 2.0$.
        3. Increase $E(R_m)$ to 12%. Observe how returns change.
        4. Decrease $E(R_m)$ to 4%. Repeat the analysis.
        """)
        
        # Button to set Lab 1 parameters
        st.button("⚡ Set Lab 1 Parameters", on_click=set_lab1_parameters, key="lab1_setup")

    # ---------------- Lab 2 ----------------
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
        1. Click "**Set Lab 2 Parameters**" to use $R_f = 3\\%$, $E(R_m) = 12\\%$, $\\beta = 2.0$.
        2. Compare expected returns for $\\beta = 1.0$ and $\\beta = 1.5$.
        3. Increase $E(R_m)$ to 15%. Observe the impact.
        4. Decrease $E(R_m)$ to 5%. Repeat the analysis.
        """)
        
        # Button to set Lab 2 parameters
        st.button("⚡ Set Lab 2 Parameters", on_click=set_lab2_parameters, key="lab2_setup")

    # ---------------- Lab 3 ----------------
    elif lab_choice == "Lab 3: Portfolio Construction":
        st.subheader("💼 Lab 3: Portfolio Construction Using CAPM")
        st.markdown("""
        **Real-World Scenario:**  
        You're constructing a portfolio with two assets: one defensive ($\\beta = 0.5$) and one aggressive ($\\beta = 2.0$).  
        How do you allocate weights to achieve a target portfolio beta?
        
        **Learning Objective:**  
        - Learn how to combine assets to achieve desired risk levels.
        - Practice calculating portfolio beta.
        
        **Suggested Steps**:
        1. Click "**Set Lab 3 Parameters**" to use $R_f = 1\\%$, $E(R_m) = 5\\%$, $\\beta = 0.5$.
        2. Allocate 60% to the defensive asset and 40% to the aggressive asset.
        3. Calculate the portfolio beta:  
           $$
           \\beta_{portfolio} = w_1 \\beta_1 + w_2 \\beta_2
           $$
        4. Adjust weights to achieve a target beta (e.g., $\\beta = 1.0$).
        """)
        
        # Button to set Lab 3 parameters
        st.button("⚡ Set Lab 3 Parameters", on_click=set_lab3_parameters, key="lab3_setup")

    # ---------------- Lab 4 ----------------
    elif lab_choice == "Lab 4: Defensive vs Aggressive Stocks":
        st.subheader("🛡️ Lab 4: Defensive vs Aggressive Stocks")
        st.markdown("""
        **Real-World Scenario:**  
        During economic downturns, defensive stocks ($\\beta < 1$) tend to outperform aggressive stocks ($\\beta > 1$).  
        How does CAPM explain this behavior?
        
        **Learning Objective:**  
        - Understand the role of beta in asset performance during market cycles.
        - Analyze the trade-off between risk and return.
        
        **Suggested Steps**:
        1. Click "**Set Lab 4 Parameters**" to use $R_f = 4\\%$, $E(R_m) = 10\\%$, $\\beta = 0.8$.
        2. Compare expected returns for $\\beta = 0.5$ and $\\beta = 1.5$.
        3. Simulate a market downturn by reducing $E(R_m)$ to 2%. Observe the impact.
        """)
        
        # Button to set Lab 4 parameters
        st.button("⚡ Set Lab 4 Parameters", on_click=set_lab4_parameters, key="lab4_setup")

    # ---------------- Lab 5 ----------------
    else:  # Lab 5: High-Risk Environments
        st.subheader("🔥 Lab 5: High-Risk Environments")
        st.markdown("""
        **Real-World Scenario:**  
        In high-volatility markets, aggressive stocks ($\\beta > 1$) can deliver outsized returns but also carry significant risk.  
        How does CAPM help you assess these opportunities?
        
        **Learning Objective:**  
        - Explore the relationship between beta and return in volatile markets.
        - Understand the importance of diversification.
        
        **Suggested Steps**:
        1. Click "**Set Lab 5 Parameters**" to use $R_f = 2\\%$, $E(R_m) = 6\\%$, $\\beta = 1.2$.
        2. Increase $E(R_m)$ to 15%. Observe the impact on expected returns.
        3. Decrease $E(R_m)$ to 1%. Repeat the analysis.
        """)
        
        # Button to set Lab 5 parameters
        st.button("⚡ Set Lab 5 Parameters", on_click=set_lab5_parameters, key="lab5_setup")

# Tab 5: The Very Basics of CAPM
with tab5:
    st.header("🧠 The Very Basics of CAPM")
    st.markdown("""
    ### 1. What Is CAPM?

    The **Capital Asset Pricing Model (CAPM)** is a tool used to estimate the expected return of an asset based on its **risk**.  
    Think of it like this:
    - Imagine you're driving a car. The **speedometer** tells you how fast you're going. Similarly, **beta** tells you how risky an asset is compared to the market.
    - If the market speeds up (higher returns), your asset might speed up too—but only if it has a high beta.

    ---

    ### 2. Why Is CAPM Important?

    CAPM helps answer a critical question:  
    **How much return should I expect for taking on a certain level of risk?**

    - **Low-risk assets** (e.g., government bonds) offer lower returns.
    - **High-risk assets** (e.g., tech stocks) offer higher returns—if they succeed.

    By using CAPM, investors can decide whether an asset is worth the risk.

    ---

    ### 3. A Simple Analogy

    Let’s say you’re at a carnival:
    - The **risk-free rate** is like playing a boring game where you always win a small prize.
    - The **market return** is like playing a more exciting game where you might win big—or lose.
    - **Beta** determines how much of the excitement (or risk) you get to experience:
      - $\\beta = 0$: You stick to the boring game.
      - $\\beta = 1$: You play the exciting game just like everyone else.
      - $\\beta > 1$: You play the exciting game with extra risk—and potentially bigger rewards.

    ---

    ### 4. How Does CAPM Work?

    The CAPM formula is:
    $$
    E(R_i) = R_f + \\beta_i (E(R_m) - R_f)
    $$
    Breaking it down:
    - **$R_f$**: The "safe" return (like parking your money in a savings account).
    - **$E(R_m)$**: The average return of the market.
    - **$\\beta_i$**: How sensitive your asset is to market movements.

    Example:
    - If $R_f = 2\\%$, $E(R_m) = 8\\%$, and $\\beta = 1.5$:
      $$
      E(R_i) = 2\\% + 1.5 (8\\% - 2\\%) = 11\\%
      $$

    ---

    ### 5. Key Takeaways

    - **CAPM** helps you estimate the expected return of an asset based on its risk.
    - **Beta** measures how sensitive an asset is to market movements.
    - **Higher beta** means higher potential returns—but also higher risk.
    - Always consider diversifying your investments to manage risk effectively.

    Remember: While CAPM is a powerful tool, it’s not perfect. Real-world markets are influenced by many factors beyond what CAPM captures.
    """)