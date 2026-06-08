import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from scipy import stats
import random

st.set_page_config(
    page_title="Financial Statement Analysis Lab",
    page_icon="📊",
    layout="wide"
)

def pct(x, d=2): return f"{round(x, d)}%"
def cr(x): return f"₹{x:,.2f} Cr"
def times(x): return f"{round(x, 2)}x"

st.title("📊 Financial Statement Analysis — Decision Making for Future-Ready Managers")
st.markdown("""
Welcome to the **Financial Statement Analysis Learning Platform**. This app covers:

- Reading & Understanding Financial Statements
- Income Statement Analysis
- Balance Sheet Analysis
- Cash Flow Statement Analysis
- Common Size Analysis (Vertical)
- Comparative Analysis (Horizontal)
- Liquidity Ratios
- Profitability Ratios
- Leverage & Solvency Ratios
- Efficiency / Activity Ratios
- Market / Valuation Ratios
- DuPont Analysis
- Cash Flow Analysis & Quality of Earnings
- Working Capital Analysis
- Trend Analysis & Forecasting
- Inter-Firm Comparison (Benchmarking)
- Red Flags & Creative Accounting
- Credit Analysis (Banker's Perspective)
- Equity Valuation from Financials
- Integrated Decision Framework

through ✅ Interactive ratio calculators ✅ DuPont decomposition ✅ Real Indian company examples
✅ Red flag detector ✅ Quiz engine ✅ Case-based learning ✅ Excel formula trainer
""")

menu = st.sidebar.radio("Choose Module", [
    "Introduction to FSA",
    "Income Statement — Reading & Analysis",
    "Balance Sheet — Reading & Analysis",
    "Cash Flow Statement Analysis",
    "Common Size Analysis",
    "Comparative (Horizontal) Analysis",
    "Liquidity Ratios",
    "Profitability Ratios",
    "Leverage & Solvency Ratios",
    "Efficiency / Activity Ratios",
    "Market & Valuation Ratios",
    "DuPont Analysis",
    "Cash Flow Quality & Earnings Quality",
    "Working Capital Analysis",
    "Trend Analysis",
    "Inter-Firm Comparison",
    "Red Flags & Creative Accounting",
    "Credit Analysis (Banker's View)",
    "Equity Valuation from Financials",
    "Integrated Decision Framework",
    "Step-by-Step Solver",
    "AI Hint System",
    "Quiz Engine",
    "Excel Formula Trainer",
    "Formula Cheat Sheet",
    "Common Student Mistakes",
    "Advanced Quiz Bank",
    "Progress Tracker",
    "Case-Based Learning — Infosys",
    "Case-Based Learning — Zomato",
])

# ── Sample Data ──────────────────────────────────────────
@st.cache_data
def get_sample_company():
    return {
        "name": "TechMfg India Ltd.",
        "IS": {
            "Revenue": 1200, "COGS": 720, "Gross_Profit": 480,
            "OPEX": 180, "EBITDA": 300, "Depreciation": 60,
            "EBIT": 240, "Interest": 48, "EBT": 192,
            "Tax": 48, "PAT": 144, "EPS": 14.4,
            "Shares": 10,  # Cr shares
        },
        "IS_prev": {
            "Revenue": 1000, "COGS": 620, "Gross_Profit": 380,
            "OPEX": 160, "EBITDA": 220, "Depreciation": 55,
            "EBIT": 165, "Interest": 40, "EBT": 125,
            "Tax": 31.25, "PAT": 93.75, "EPS": 9.375,
        },
        "BS": {
            # Assets
            "Cash": 80, "Debtors": 200, "Inventory": 150, "Other_CA": 20,
            "Total_CA": 450, "Net_FA": 600, "CWIP": 50, "Investments": 100,
            "Other_NCA": 50, "Total_NCA": 800, "Total_Assets": 1250,
            # Liabilities
            "Creditors": 120, "Short_Debt": 80, "Other_CL": 30,
            "Total_CL": 230, "Long_Debt": 400, "Deferred_Tax": 30,
            "Other_NCL": 20, "Total_NCL": 450,
            # Equity
            "Share_Capital": 100, "Reserves": 470,
            "Total_Equity": 570, "Total_LE": 1250,
        },
        "BS_prev": {
            "Cash": 60, "Debtors": 170, "Inventory": 130, "Other_CA": 18,
            "Total_CA": 378, "Net_FA": 570, "CWIP": 80, "Investments": 90,
            "Other_NCA": 45, "Total_NCA": 785, "Total_Assets": 1163,
            "Creditors": 100, "Short_Debt": 70, "Other_CL": 25,
            "Total_CL": 195, "Long_Debt": 420, "Deferred_Tax": 28,
            "Other_NCL": 18, "Total_NCL": 466,
            "Share_Capital": 100, "Reserves": 402,
            "Total_Equity": 502, "Total_LE": 1163,
        },
        "CF": {
            "Net_Income": 144, "Depreciation": 60, "WC_Changes": -30,
            "Other_Operating": -10, "CFO": 164,
            "Capex": -90, "Investments": -10, "CFI": -100,
            "Borrowings": -20, "Dividends": -30, "CFF": -50,
            "Net_CF": 14,
        },
        "Market": {
            "Share_Price": 280, "PE_Industry": 22,
            "EV_EBITDA_Industry": 14,
        }
    }

data = get_sample_company()

# =========================================================
if menu == "Introduction to FSA":
    st.header("📘 Introduction to Financial Statement Analysis")
    st.markdown("""
## What is Financial Statement Analysis?

**FSA** is the process of reviewing and evaluating a company's financial statements
to make informed **economic decisions** — whether to invest, lend, acquire, or partner.

## The Three Core Statements

| Statement | Purpose | Answers |
|---|---|---|
| **Income Statement (P&L)** | Profitability over a period | Did the company make money? How much? |
| **Balance Sheet** | Financial position at a point in time | What does the company own and owe? |
| **Cash Flow Statement** | Cash generated and used | Is the company cash-generating? |

## Who Uses FSA and Why?

| User | Decision | Key Focus |
|---|---|---|
| **Equity Investor** | Buy / Hold / Sell | Profitability, Growth, Valuation |
| **Banker / Lender** | Lend or not; at what rate | Liquidity, Solvency, Cash Flow |
| **Competitor** | Benchmark | Margins, Efficiency, Market Share |
| **Manager** | Operational decisions | All ratios + KPIs |
| **Supplier** | Extend credit | Liquidity, Payment history |
| **Regulator** | Compliance | Reporting quality, Disclosures |
| **M&A Analyst** | Acquire or merge | Enterprise Value, Synergies |

## The FSA Process — 5 Steps

1. **Collect** the annual report, quarterly filings, conference call transcripts
2. **Read** the financial statements + notes to accounts
3. **Calculate** ratios — compare to prior years & industry peers
4. **Identify** trends, red flags, strengths & weaknesses
5. **Conclude** — make the decision (invest / lend / partner)

## Key Indian Sources

- **BSE / NSE filings** — Quarterly and Annual Results
- **MCA21** — Financial filings of all companies
- **Screener.in** — Free ratio database for Indian companies
- **Moneycontrol / Tickertape** — Retail investor tools
- **Bloomberg / Capital IQ** — Professional tools
- **RBI CMIE / CRISIL** — Sector benchmarks
""")

    col1, col2 = st.columns(2)
    col1.success("""
**Limitations of FSA:**
- Historical data — past ≠ future
- Accounting policies vary across firms
- Creative accounting can distort ratios
- Off-balance-sheet items not visible
- Non-financial factors (management, brand) excluded
""")
    col2.warning("""
**Key Principle: Always Compare**
- Compare to OWN HISTORY (trend analysis)
- Compare to INDUSTRY PEERS (benchmarking)
- Compare to INDUSTRY AVERAGE (sectoral norms)
- NEVER analyse a ratio in isolation
""")

# =========================================================
elif menu == "Income Statement — Reading & Analysis":
    st.header("📋 Income Statement — Reading & Analysis")

    st.subheader("🔢 Build Your Income Statement")
    col1, col2 = st.columns(2)
    with col1:
        rev = st.number_input("Revenue / Net Sales (₹ Cr)", value=float(data["IS"]["Revenue"]))
        cogs = st.number_input("Cost of Goods Sold / COGS (₹ Cr)", value=float(data["IS"]["COGS"]))
        opex = st.number_input("Operating Expenses (₹ Cr)", value=float(data["IS"]["OPEX"]))
        dep = st.number_input("Depreciation & Amortisation (₹ Cr)", value=float(data["IS"]["Depreciation"]))
        interest = st.number_input("Interest / Finance Cost (₹ Cr)", value=float(data["IS"]["Interest"]))
        tax_rate = st.number_input("Effective Tax Rate (%)", value=25.0)
        shares = st.number_input("Shares Outstanding (Cr)", value=float(data["IS"]["Shares"]))
    with col2:
        gp = rev - cogs
        ebitda = gp - opex
        ebit = ebitda - dep
        ebt = ebit - interest
        tax = max(ebt * tax_rate/100, 0)
        pat = ebt - tax
        eps = pat / shares if shares > 0 else 0

        is_df = pd.DataFrame({
            "Line Item": ["Revenue","(-) COGS","= Gross Profit","(-) Operating Expenses",
                          "= EBITDA","(-) Depreciation","= EBIT",
                          "(-) Interest","= EBT","(-) Tax","= PAT (Net Profit)","EPS (₹)"],
            "Amount (₹ Cr)": [cr(rev), cr(-cogs), cr(gp), cr(-opex),
                               cr(ebitda), cr(-dep), cr(ebit),
                               cr(-interest), cr(ebt), cr(-tax), cr(pat), f"₹{round(eps,2)}"],
            "% of Revenue": [pct(100), pct(cogs/rev*100), pct(gp/rev*100),
                              pct(opex/rev*100), pct(ebitda/rev*100),
                              pct(dep/rev*100), pct(ebit/rev*100),
                              pct(interest/rev*100), pct(ebt/rev*100),
                              pct(tax/rev*100 if rev>0 else 0),
                              pct(pat/rev*100 if rev>0 else 0), "—"]
        })
        st.dataframe(is_df, use_container_width=True)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Gross Margin", pct(gp/rev*100) if rev>0 else "—")
    col2.metric("EBITDA Margin", pct(ebitda/rev*100) if rev>0 else "—")
    col3.metric("EBIT Margin", pct(ebit/rev*100) if rev>0 else "—")
    col4.metric("Net Profit Margin", pct(pat/rev*100) if rev>0 else "—")

    st.subheader("Waterfall Chart — Revenue to PAT")
    fig = go.Figure(go.Waterfall(
        orientation="v",
        measure=["absolute","relative","total","relative","total",
                 "relative","total","relative","total"],
        x=["Revenue","COGS","Gross Profit","OPEX+D&A","EBIT","Interest","EBT","Tax","PAT"],
        y=[rev, -cogs, 0, -(opex+dep), 0, -interest, 0, -tax, 0],
        connector={"line":{"color":"navy"}},
        decreasing={"marker":{"color":"#C03B3B"}},
        increasing={"marker":{"color":"#157A42"}},
        totals={"marker":{"color":"#174EA6"}}
    ))
    fig.update_layout(title="Revenue to PAT — Waterfall", height=380)
    st.plotly_chart(fig, use_container_width=True)

    with st.expander("📘 Key Concepts — Income Statement"):
        st.markdown("""
**Gross Profit** = Revenue − COGS (measures core product/service profitability)

**EBITDA** = Earnings Before Interest, Tax, Depreciation & Amortisation
- Proxy for operating cash flow
- Used in EV/EBITDA valuation multiple

**EBIT** = Earnings Before Interest & Tax (= Operating Profit)

**Interest Coverage Ratio (ICR)** = EBIT / Interest (must be > 2x for healthy firm)

**EPS** = PAT / Shares — most watched metric by equity analysts

**Operating Leverage:** High fixed costs → EBITDA grows faster than revenue
""")

# =========================================================
elif menu == "Balance Sheet — Reading & Analysis":
    st.header("📊 Balance Sheet — Reading & Analysis")

    st.subheader("🔢 Balance Sheet Builder")
    col1, col2, col3 = st.columns(3)
    bs = data["BS"]
    with col1:
        st.markdown("**Current Assets (₹ Cr)**")
        cash = st.number_input("Cash & Equivalents", value=float(bs["Cash"]))
        debtors = st.number_input("Trade Receivables", value=float(bs["Debtors"]))
        inventory = st.number_input("Inventory", value=float(bs["Inventory"]))
        other_ca = st.number_input("Other Current Assets", value=float(bs["Other_CA"]))
        total_ca = cash + debtors + inventory + other_ca

        st.markdown("**Non-Current Assets (₹ Cr)**")
        net_fa = st.number_input("Net Fixed Assets (PP&E)", value=float(bs["Net_FA"]))
        investments = st.number_input("Long-term Investments", value=float(bs["Investments"]))
        other_nca = st.number_input("Other Non-Current Assets", value=float(bs["Other_NCA"]))
        total_nca = net_fa + investments + other_nca
        total_assets = total_ca + total_nca

    with col2:
        st.markdown("**Current Liabilities (₹ Cr)**")
        creditors = st.number_input("Trade Payables", value=float(bs["Creditors"]))
        short_debt = st.number_input("Short-term Borrowings", value=float(bs["Short_Debt"]))
        other_cl = st.number_input("Other Current Liabilities", value=float(bs["Other_CL"]))
        total_cl = creditors + short_debt + other_cl

        st.markdown("**Non-Current Liabilities (₹ Cr)**")
        long_debt = st.number_input("Long-term Debt", value=float(bs["Long_Debt"]))
        deferred_tax = st.number_input("Deferred Tax Liability", value=float(bs["Deferred_Tax"]))
        other_ncl = st.number_input("Other Non-Current Liabilities", value=float(bs["Other_NCL"]))
        total_ncl = long_debt + deferred_tax + other_ncl

        st.markdown("**Equity (₹ Cr)**")
        share_capital = st.number_input("Share Capital", value=float(bs["Share_Capital"]))
        reserves = st.number_input("Reserves & Surplus", value=float(bs["Reserves"]))
        total_equity = share_capital + reserves
        total_le = total_cl + total_ncl + total_equity

    with col3:
        st.markdown("**Balance Sheet Summary**")
        bs_summary = pd.DataFrame({
            "Item": ["Cash","Debtors","Inventory","Other CA","TOTAL CA",
                     "Net FA","Investments","Other NCA","TOTAL NCA",
                     "TOTAL ASSETS","","Trade Payables","Short-term Debt","Other CL",
                     "TOTAL CL","Long-term Debt","Other NCL","TOTAL NCL",
                     "Share Capital","Reserves","TOTAL EQUITY","TOTAL L+E"],
            "₹ Cr": [cash,debtors,inventory,other_ca,total_ca,
                      net_fa,investments,other_nca,total_nca,total_assets,"",
                      creditors,short_debt,other_cl,total_cl,
                      long_debt,other_ncl+deferred_tax,total_ncl,
                      share_capital,reserves,total_equity,total_le]
        })
        bs_summary["₹ Cr"] = bs_summary["₹ Cr"].apply(lambda x: cr(x) if x != "" else "")
        st.dataframe(bs_summary, use_container_width=True)

        if abs(total_assets - total_le) < 0.01:
            st.success("✅ Balance Sheet balances!")
        else:
            st.error(f"❌ Imbalance: Assets={cr(total_assets)}, L+E={cr(total_le)}")

    col1, col2, col3 = st.columns(3)
    total_debt = short_debt + long_debt
    col1.metric("Total Debt", cr(total_debt))
    col2.metric("D/E Ratio", times(total_debt/total_equity) if total_equity>0 else "—")
    col3.metric("Net Debt", cr(total_debt - cash))

    fig = go.Figure()
    fig.add_trace(go.Bar(name='Assets', x=['Current','Non-Current'],
                          y=[total_ca, total_nca], marker_color=['#174EA6','#0D1B3E']))
    fig.add_trace(go.Bar(name='Liabilities+Equity', x=['Current','Non-Current+Equity'],
                          y=[total_cl, total_ncl+total_equity], marker_color=['#C03B3B','#157A42']))
    fig.update_layout(barmode='group', title="Asset vs Liability Structure", height=300)
    st.plotly_chart(fig, use_container_width=True)

# =========================================================
elif menu == "Cash Flow Statement Analysis":
    st.header("💵 Cash Flow Statement Analysis")
    st.markdown("""
## The Cash Flow Statement — Structure

| Section | What It Shows |
|---|---|
| **Operating CF (CFO)** | Cash from core business operations |
| **Investing CF (CFI)** | Cash used for / from investments, capex |
| **Financing CF (CFF)** | Cash from/to shareholders and lenders |

**Most important principle:** PAT ≠ Cash Flow. Profitability ≠ Liquidity.
""")

    col1, col2 = st.columns(2)
    cf = data["CF"]
    with col1:
        st.subheader("Build Cash Flow Statement")
        net_inc = st.number_input("Net Income / PAT (₹ Cr)", value=float(cf["Net_Income"]))
        dep_cf = st.number_input("Add: Depreciation (₹ Cr)", value=float(cf["Depreciation"]))
        wc_change = st.number_input("Changes in Working Capital (₹ Cr, negative = uses cash)", value=float(cf["WC_Changes"]))
        other_op = st.number_input("Other Operating Adjustments (₹ Cr)", value=float(cf["Other_Operating"]))
        cfo = net_inc + dep_cf + wc_change + other_op

        capex = st.number_input("Capital Expenditure (₹ Cr, enter negative)", value=float(cf["Capex"]))
        inv_cf = st.number_input("Investment Activities (₹ Cr)", value=float(cf["Investments"]))
        cfi = capex + inv_cf

        borrowings = st.number_input("Net Borrowings (₹ Cr)", value=float(cf["Borrowings"]))
        dividends = st.number_input("Dividends Paid (₹ Cr, enter negative)", value=float(cf["Dividends"]))
        cff = borrowings + dividends
        net_cf = cfo + cfi + cff

    with col2:
        cf_df = pd.DataFrame({
            "Section": ["Net Income","(+) Depreciation","(+/-) WC Changes","Other",
                        "= OPERATING CF (CFO)","CapEx","Investments",
                        "= INVESTING CF (CFI)","Net Borrowings","Dividends",
                        "= FINANCING CF (CFF)","NET CHANGE IN CASH"],
            "₹ Cr": [net_inc, dep_cf, wc_change, other_op, cfo,
                      capex, inv_cf, cfi, borrowings, dividends, cff, net_cf]
        })
        cf_df["₹ Cr"] = cf_df["₹ Cr"].apply(lambda x: cr(x))
        st.dataframe(cf_df, use_container_width=True)

        fcf = cfo + capex
        cfo_pct = cfo/net_inc*100 if net_inc>0 else 0

        st.metric("Free Cash Flow (FCF)", cr(fcf))
        st.metric("CFO/PAT Ratio", pct(cfo_pct))

        if cfo > net_inc * 0.8:
            st.success("✅ CFO > 80% of PAT — Good earnings quality")
        else:
            st.warning("⚠️ CFO < PAT — Check working capital or accruals")

    st.subheader("CF Pattern Diagnosis")
    cf_patterns = {
        "(+) CFO, (−) CFI, (−) CFF": "🟢 Mature company — self-funding growth, repaying debt",
        "(+) CFO, (−) CFI, (+) CFF": "🟡 Growing company — needs external capital for expansion",
        "(−) CFO, (−) CFI, (+) CFF": "🔴 Early stage / distressed — burning cash, raising capital",
        "(+) CFO, (+) CFI, (−) CFF": "🔵 Asset-light / harvesting — selling assets, returning cash",
    }
    current_pattern = f"{'(+)' if cfo>0 else '(−)'} CFO, {'(+)' if cfi>0 else '(−)'} CFI, {'(+)' if cff>0 else '(−)'} CFF"
    st.info(f"**Your pattern:** {current_pattern}")
    for pattern, meaning in cf_patterns.items():
        if pattern == current_pattern:
            st.success(f"**Match:** {meaning}")

# =========================================================
elif menu == "Common Size Analysis":
    st.header("📐 Common Size Analysis (Vertical Analysis)")
    st.markdown("""
## What is Common Size Analysis?

**Common size** expresses every line item as a **percentage of a base figure**:
- Income Statement: % of **Revenue**
- Balance Sheet: % of **Total Assets**

**Purpose:** Compare firms of different sizes; identify structural changes over time.
""")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Income Statement — Common Size")
        is_data = data["IS"]
        is_prev = data["IS_prev"]
        rev_curr = is_data["Revenue"]; rev_prev = is_prev["Revenue"]

        items_is = ["Revenue","COGS","Gross_Profit","OPEX","EBITDA","Depreciation","EBIT","Interest","EBT","Tax","PAT"]
        cs_is = pd.DataFrame({
            "Item": items_is,
            "Current (₹Cr)": [is_data[i] for i in items_is],
            "% Revenue (Curr)": [pct(is_data[i]/rev_curr*100) for i in items_is],
            "Prior (₹Cr)": [is_prev.get(i,0) for i in items_is],
            "% Revenue (Prior)": [pct(is_prev.get(i,0)/rev_prev*100) for i in items_is],
        })
        st.dataframe(cs_is, use_container_width=True)

    with col2:
        st.subheader("Balance Sheet — Common Size")
        bs_curr = data["BS"]; bs_prev = data["BS_prev"]
        ta_curr = bs_curr["Total_Assets"]; ta_prev = bs_prev["Total_Assets"]
        items_bs = ["Cash","Debtors","Inventory","Total_CA","Net_FA","Total_Assets",
                    "Total_CL","Long_Debt","Total_Equity"]
        cs_bs = pd.DataFrame({
            "Item": items_bs,
            "Current (₹Cr)": [bs_curr[i] for i in items_bs],
            "% Total Assets": [pct(bs_curr[i]/ta_curr*100) for i in items_bs],
            "Prior (₹Cr)": [bs_prev[i] for i in items_bs],
            "% Total Assets (Prior)": [pct(bs_prev[i]/ta_prev*100) for i in items_bs],
        })
        st.dataframe(cs_bs, use_container_width=True)

    st.subheader("Cost Structure Pie Chart")
    fig = go.Figure(go.Pie(
        labels=["COGS","OPEX","Depreciation","Interest","Tax","PAT"],
        values=[is_data["COGS"], is_data["OPEX"], is_data["Depreciation"],
                is_data["Interest"], is_data["Tax"], is_data["PAT"]],
        hole=0.4
    ))
    fig.update_layout(title="Revenue Breakdown — Current Year", height=350)
    st.plotly_chart(fig, use_container_width=True)

# =========================================================
elif menu == "Comparative (Horizontal) Analysis":
    st.header("📈 Comparative (Horizontal) Analysis")
    st.markdown("""
## What is Horizontal Analysis?

Compare each line item **year-over-year** — calculate absolute change and % change.

**Purpose:** Identify growth rates, accelerating/decelerating trends, structural shifts.
""")

    is_d = data["IS"]; is_p = data["IS_prev"]
    items = ["Revenue","COGS","Gross_Profit","OPEX","EBITDA","EBIT","Interest","PAT"]
    horiz_df = pd.DataFrame({
        "Item": items,
        "Prior Year (₹Cr)": [is_p.get(i,0) for i in items],
        "Current Year (₹Cr)": [is_d.get(i,0) for i in items],
        "Change (₹Cr)": [is_d.get(i,0)-is_p.get(i,0) for i in items],
        "% Change": [pct((is_d.get(i,0)-is_p.get(i,0))/is_p.get(i,0)*100 if is_p.get(i,0)!=0 else 0) for i in items]
    })
    st.dataframe(horiz_df, use_container_width=True)

    # Revenue growth vs PAT growth
    rev_growth = (is_d["Revenue"]-is_p["Revenue"])/is_p["Revenue"]*100
    pat_growth = (is_d["PAT"]-is_p["PAT"])/is_p["PAT"]*100
    ebitda_growth = (is_d["EBITDA"]-is_p["EBITDA"])/is_p["EBITDA"]*100

    col1, col2, col3 = st.columns(3)
    col1.metric("Revenue Growth", pct(rev_growth))
    col2.metric("EBITDA Growth", pct(ebitda_growth))
    col3.metric("PAT Growth", pct(pat_growth))

    if pat_growth > rev_growth:
        st.success(f"✅ PAT ({pct(pat_growth)}) growing FASTER than Revenue ({pct(rev_growth)}) — Operating leverage working!")
    else:
        st.warning(f"⚠️ PAT ({pct(pat_growth)}) growing SLOWER than Revenue ({pct(rev_growth)}) — Margin compression?")

    fig = go.Figure()
    categories = items
    fig.add_trace(go.Bar(name='Prior Year', x=categories,
                          y=[is_p.get(i,0) for i in items], marker_color='#B5CCFF'))
    fig.add_trace(go.Bar(name='Current Year', x=categories,
                          y=[is_d.get(i,0) for i in items], marker_color='#174EA6'))
    fig.update_layout(barmode='group', title="Year-over-Year Comparison",
                      xaxis_title="Line Item", yaxis_title="₹ Crore")
    st.plotly_chart(fig, use_container_width=True)

# =========================================================
elif menu == "Liquidity Ratios":
    st.header("💧 Liquidity Ratios")
    st.markdown("""
## Liquidity Ratios — Can the Company Pay Short-term Obligations?

| Ratio | Formula | Benchmark |
|---|---|---|
| **Current Ratio** | Current Assets / Current Liabilities | 1.5–2.0x |
| **Quick Ratio** | (CA − Inventory) / CL | ≥ 1.0x |
| **Cash Ratio** | (Cash + Marketable Securities) / CL | ≥ 0.5x |
| **CCC** | DIO + DSO − DPO | Lower is better |
""")

    col1, col2 = st.columns(2)
    bs = data["BS"]; is_d = data["IS"]
    with col1:
        ca = st.number_input("Current Assets (₹ Cr)", value=float(bs["Total_CA"]))
        inventory = st.number_input("Inventory (₹ Cr)", value=float(bs["Inventory"]))
        cash = st.number_input("Cash (₹ Cr)", value=float(bs["Cash"]))
        cl = st.number_input("Current Liabilities (₹ Cr)", value=float(bs["Total_CL"]))
        revenue_liq = st.number_input("Revenue (₹ Cr)", value=float(is_d["Revenue"]))
        cogs_liq = st.number_input("COGS (₹ Cr)", value=float(is_d["COGS"]))
        debtors_liq = st.number_input("Trade Receivables (₹ Cr)", value=float(bs["Debtors"]))
        creditors_liq = st.number_input("Trade Payables (₹ Cr)", value=float(bs["Creditors"]))

    cr_ratio = ca / cl if cl > 0 else 0
    qr_ratio = (ca - inventory) / cl if cl > 0 else 0
    cash_ratio = cash / cl if cl > 0 else 0
    dso = debtors_liq / (revenue_liq/365) if revenue_liq > 0 else 0
    dio = inventory / (cogs_liq/365) if cogs_liq > 0 else 0
    dpo = creditors_liq / (cogs_liq/365) if cogs_liq > 0 else 0
    ccc = dso + dio - dpo

    with col2:
        ratios_liq = pd.DataFrame({
            "Ratio": ["Current Ratio","Quick Ratio","Cash Ratio",
                      "Days Sales Outstanding (DSO)","Days Inventory Outstanding (DIO)",
                      "Days Payable Outstanding (DPO)","Cash Conversion Cycle (CCC)"],
            "Value": [times(cr_ratio), times(qr_ratio), times(cash_ratio),
                      f"{round(dso,1)} days", f"{round(dio,1)} days",
                      f"{round(dpo,1)} days", f"{round(ccc,1)} days"],
            "Benchmark": ["1.5-2.0x","≥1.0x","≥0.5x","<45 days","<60 days",">30 days","<60 days"],
            "Status": [
                "✅" if 1.5 <= cr_ratio <= 3.0 else ("⚠️ Too low" if cr_ratio < 1.5 else "⚠️ Too high"),
                "✅" if qr_ratio >= 1.0 else "❌",
                "✅" if cash_ratio >= 0.5 else "⚠️",
                "✅" if dso <= 45 else "⚠️",
                "✅" if dio <= 60 else "⚠️",
                "✅" if dpo >= 30 else "⚠️",
                "✅" if ccc <= 60 else "⚠️"
            ]
        })
        st.dataframe(ratios_liq, use_container_width=True)

    st.subheader("CCC Deep Dive")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("DSO", f"{round(dso,1)} days")
    col2.metric("DIO", f"{round(dio,1)} days")
    col3.metric("DPO", f"{round(dpo,1)} days")
    col4.metric("CCC", f"{round(ccc,1)} days")
    st.info(f"Reducing CCC by 10 days frees up ₹{round(revenue_liq*10/365,2)}Cr of cash at this revenue level.")

# =========================================================
elif menu == "Profitability Ratios":
    st.header("📈 Profitability Ratios")
    st.markdown("""
## Profitability Ratios — Is the Company Earning Enough?

| Ratio | Formula | What It Measures |
|---|---|---|
| **Gross Margin** | Gross Profit / Revenue | Core product profitability |
| **EBITDA Margin** | EBITDA / Revenue | Operating cash profitability |
| **EBIT Margin** | EBIT / Revenue | Operating profitability |
| **Net Margin** | PAT / Revenue | Bottom-line profitability |
| **ROE** | PAT / Equity | Return to shareholders |
| **ROA** | PAT / Total Assets | Return on all capital |
| **ROCE** | EBIT / Capital Employed | Return on all capital deployed |
""")

    col1, col2 = st.columns(2)
    is_d = data["IS"]; bs = data["BS"]
    with col1:
        rev_p = st.number_input("Revenue (₹ Cr)", value=float(is_d["Revenue"]), key="prof_rev")
        gp_p = st.number_input("Gross Profit (₹ Cr)", value=float(is_d["Gross_Profit"]))
        ebitda_p = st.number_input("EBITDA (₹ Cr)", value=float(is_d["EBITDA"]))
        ebit_p = st.number_input("EBIT (₹ Cr)", value=float(is_d["EBIT"]))
        pat_p = st.number_input("PAT (₹ Cr)", value=float(is_d["PAT"]))
        equity_p = st.number_input("Total Equity (₹ Cr)", value=float(bs["Total_Equity"]))
        assets_p = st.number_input("Total Assets (₹ Cr)", value=float(bs["Total_Assets"]))
        total_debt_p = st.number_input("Total Debt (₹ Cr)",
                                        value=float(bs["Short_Debt"]+bs["Long_Debt"]))

    gross_margin = gp_p/rev_p*100 if rev_p>0 else 0
    ebitda_margin = ebitda_p/rev_p*100 if rev_p>0 else 0
    ebit_margin = ebit_p/rev_p*100 if rev_p>0 else 0
    net_margin = pat_p/rev_p*100 if rev_p>0 else 0
    roe = pat_p/equity_p*100 if equity_p>0 else 0
    roa = pat_p/assets_p*100 if assets_p>0 else 0
    capital_employed = equity_p + total_debt_p
    roce = ebit_p/capital_employed*100 if capital_employed>0 else 0

    with col2:
        prof_df = pd.DataFrame({
            "Ratio": ["Gross Margin","EBITDA Margin","EBIT Margin","Net Profit Margin",
                      "Return on Equity (ROE)","Return on Assets (ROA)","ROCE"],
            "Value": [pct(gross_margin), pct(ebitda_margin), pct(ebit_margin),
                      pct(net_margin), pct(roe), pct(roa), pct(roce)],
            "Industry Benchmark": ["30-40%","18-22%","15-18%","10-15%",
                                    "15-20%","8-12%","12-18%"],
        })
        st.dataframe(prof_df, use_container_width=True)

        fig = go.Figure(go.Bar(
            x=["Gross Margin","EBITDA Margin","EBIT Margin","Net Margin","ROE","ROA","ROCE"],
            y=[gross_margin, ebitda_margin, ebit_margin, net_margin, roe, roa, roce],
            marker_color=['#157A42' if v>12 else '#F5A623' if v>6 else '#C03B3B'
                          for v in [gross_margin,ebitda_margin,ebit_margin,net_margin,roe,roa,roce]]
        ))
        fig.update_layout(title="Profitability Ratios", yaxis_title="%", height=300)
        st.plotly_chart(fig, use_container_width=True)

# =========================================================
elif menu == "Leverage & Solvency Ratios":
    st.header("⚖️ Leverage & Solvency Ratios")
    st.markdown("""
## Leverage Ratios — How Much Debt?

| Ratio | Formula | Safe Benchmark |
|---|---|---|
| **Debt-to-Equity (D/E)** | Total Debt / Total Equity | < 1.5x |
| **Debt-to-Assets** | Total Debt / Total Assets | < 50% |
| **Debt-to-EBITDA** | Net Debt / EBITDA | < 3x |
| **Interest Coverage (ICR)** | EBIT / Interest | > 3x |
| **DSCR** | Net Operating CF / Total Debt Service | > 1.25x |
| **Financial Leverage** | Total Assets / Equity | Shows leverage multiplier |
""")

    col1, col2 = st.columns(2)
    bs = data["BS"]; is_d = data["IS"]
    with col1:
        short_d = st.number_input("Short-term Debt (₹ Cr)", value=float(bs["Short_Debt"]))
        long_d = st.number_input("Long-term Debt (₹ Cr)", value=float(bs["Long_Debt"]))
        equity_l = st.number_input("Total Equity (₹ Cr)", value=float(bs["Total_Equity"]))
        assets_l = st.number_input("Total Assets (₹ Cr)", value=float(bs["Total_Assets"]))
        ebit_l = st.number_input("EBIT (₹ Cr)", value=float(is_d["EBIT"]))
        ebitda_l = st.number_input("EBITDA (₹ Cr)", value=float(is_d["EBITDA"]))
        interest_l = st.number_input("Interest Expense (₹ Cr)", value=float(is_d["Interest"]))
        cash_l = st.number_input("Cash (₹ Cr)", value=float(bs["Cash"]))
        cfo_l = st.number_input("Operating Cash Flow (₹ Cr)", value=164.0)

    total_d = short_d + long_d
    net_d = total_d - cash_l
    de_ratio = total_d / equity_l if equity_l > 0 else 0
    da_ratio = total_d / assets_l * 100 if assets_l > 0 else 0
    debt_ebitda = net_d / ebitda_l if ebitda_l > 0 else 0
    icr = ebit_l / interest_l if interest_l > 0 else 0
    debt_service = interest_l + short_d*0.2  # simplified principal
    dscr = cfo_l / debt_service if debt_service > 0 else 0
    fin_leverage = assets_l / equity_l if equity_l > 0 else 0

    with col2:
        lev_df = pd.DataFrame({
            "Ratio": ["D/E Ratio","Debt/Assets","Net Debt/EBITDA",
                      "Interest Coverage (ICR)","DSCR","Financial Leverage"],
            "Value": [times(de_ratio), pct(da_ratio), times(debt_ebitda),
                      times(icr), times(dscr), times(fin_leverage)],
            "Safe Benchmark": ["<1.5x","<50%","<3x",">3x",">1.25x","<3x"],
            "Status": [
                "✅" if de_ratio < 1.5 else "❌",
                "✅" if da_ratio < 50 else "❌",
                "✅" if debt_ebitda < 3 else "❌",
                "✅" if icr > 3 else ("⚠️" if icr > 1.5 else "❌"),
                "✅" if dscr > 1.25 else "❌",
                "✅" if fin_leverage < 3 else "⚠️"
            ]
        })
        st.dataframe(lev_df, use_container_width=True)

    if icr < 1.5:
        st.error(f"❌ ICR = {round(icr,2)}x — Dangerously low! Company may struggle to service debt.")
    elif icr < 3:
        st.warning(f"⚠️ ICR = {round(icr,2)}x — Below comfortable level. Monitor debt serviceability.")
    else:
        st.success(f"✅ ICR = {round(icr,2)}x — Healthy interest coverage.")

# =========================================================
elif menu == "Efficiency / Activity Ratios":
    st.header("⚙️ Efficiency / Activity Ratios")
    st.markdown("""
## Efficiency Ratios — How Well Does the Company Use its Assets?

| Ratio | Formula | What it Measures |
|---|---|---|
| **Asset Turnover** | Revenue / Total Assets | Revenue generated per ₹ of assets |
| **Fixed Asset Turnover** | Revenue / Net FA | Productivity of fixed assets |
| **Inventory Turnover** | COGS / Inventory | How fast inventory is sold |
| **Receivables Turnover** | Revenue / Debtors | How fast debtors pay |
| **Payables Turnover** | COGS / Creditors | How fast the company pays |
""")

    col1, col2 = st.columns(2)
    is_d = data["IS"]; bs = data["BS"]
    with col1:
        rev_e = st.number_input("Revenue (₹ Cr)", value=float(is_d["Revenue"]), key="eff_rev")
        cogs_e = st.number_input("COGS (₹ Cr)", value=float(is_d["COGS"]), key="eff_cogs")
        assets_e = st.number_input("Total Assets (₹ Cr)", value=float(bs["Total_Assets"]), key="eff_a")
        fa_e = st.number_input("Net Fixed Assets (₹ Cr)", value=float(bs["Net_FA"]))
        inv_e = st.number_input("Inventory (₹ Cr)", value=float(bs["Inventory"]), key="eff_inv")
        deb_e = st.number_input("Trade Receivables (₹ Cr)", value=float(bs["Debtors"]), key="eff_deb")
        cred_e = st.number_input("Trade Payables (₹ Cr)", value=float(bs["Creditors"]), key="eff_cred")

    asset_turn = rev_e/assets_e if assets_e>0 else 0
    fa_turn = rev_e/fa_e if fa_e>0 else 0
    inv_turn = cogs_e/inv_e if inv_e>0 else 0
    rec_turn = rev_e/deb_e if deb_e>0 else 0
    pay_turn = cogs_e/cred_e if cred_e>0 else 0
    dio_e = 365/inv_turn if inv_turn>0 else 0
    dso_e = 365/rec_turn if rec_turn>0 else 0
    dpo_e = 365/pay_turn if pay_turn>0 else 0

    with col2:
        eff_df = pd.DataFrame({
            "Ratio": ["Asset Turnover","Fixed Asset Turnover","Inventory Turnover",
                      "Receivables Turnover","Payables Turnover",
                      "Days Inventory (DIO)","Days Receivables (DSO)","Days Payables (DPO)"],
            "Value": [times(asset_turn), times(fa_turn), times(inv_turn),
                      times(rec_turn), times(pay_turn),
                      f"{round(dio_e,1)}d", f"{round(dso_e,1)}d", f"{round(dpo_e,1)}d"],
            "Better When": ["Higher","Higher","Higher (but not too high)","Higher","Lower",
                             "Lower","Lower","Higher (more supplier credit)"]
        })
        st.dataframe(eff_df, use_container_width=True)

# =========================================================
elif menu == "Market & Valuation Ratios":
    st.header("💹 Market & Valuation Ratios")
    st.markdown("""
## Market Ratios — Is the Stock Expensive or Cheap?

| Ratio | Formula | Use |
|---|---|---|
| **P/E Ratio** | Market Price / EPS | Main valuation multiple |
| **P/B Ratio** | Market Price / Book Value per share | Asset-heavy industries |
| **EV/EBITDA** | Enterprise Value / EBITDA | Capital structure independent |
| **EV/Revenue** | Enterprise Value / Revenue | For loss-making companies |
| **Dividend Yield** | DPS / Market Price | Income investors |
| **PEG Ratio** | P/E / Earnings Growth Rate | Growth-adjusted valuation |
""")

    col1, col2 = st.columns(2)
    is_d = data["IS"]; bs = data["BS"]; mkt = data["Market"]
    with col1:
        price = st.number_input("Market Share Price (₹)", value=float(mkt["Share_Price"]))
        shares_mv = st.number_input("Shares Outstanding (Cr)", value=float(is_d["Shares"]))
        eps_mv = st.number_input("EPS (₹)", value=float(is_d["EPS"]))
        bvps = (bs["Total_Equity"]*1e7) / (shares_mv*1e7) if shares_mv>0 else 0
        ebitda_mv = st.number_input("EBITDA (₹ Cr)", value=float(is_d["EBITDA"]), key="mv_ebitda")
        rev_mv = st.number_input("Revenue (₹ Cr)", value=float(is_d["Revenue"]), key="mv_rev")
        total_d_mv = st.number_input("Total Debt (₹ Cr)", value=float(bs["Short_Debt"]+bs["Long_Debt"]))
        cash_mv = st.number_input("Cash (₹ Cr)", value=float(bs["Cash"]), key="mv_cash")
        dps = st.number_input("Dividend Per Share (₹)", value=3.0)
        growth_rate = st.number_input("EPS Growth Rate (%)", value=15.0)

    market_cap = price * shares_mv
    ev = market_cap + total_d_mv - cash_mv
    pe = price/eps_mv if eps_mv>0 else 0
    pb = price/bvps if bvps>0 else 0
    ev_ebitda = ev*1e7 / (ebitda_mv*1e7) if ebitda_mv>0 else 0
    ev_rev = ev*1e7 / (rev_mv*1e7) if rev_mv>0 else 0
    div_yield = dps/price*100 if price>0 else 0
    peg = pe/growth_rate if growth_rate>0 else 0

    with col2:
        mv_df = pd.DataFrame({
            "Ratio": ["Market Cap","Enterprise Value (EV)","P/E Ratio",
                      "P/B Ratio","EV/EBITDA","EV/Revenue","Dividend Yield","PEG Ratio"],
            "Your Company": [cr(market_cap), cr(ev), times(pe), times(pb),
                              times(ev_ebitda), times(ev_rev), pct(div_yield), round(peg,2)],
            "Industry Benchmark": ["—","—",f"{mkt['PE_Industry']}x","2-4x",
                                    f"{mkt['EV_EBITDA_Industry']}x","3-5x","1-2%","<1.5 = fair"],
            "Signal": [
                "—", "—",
                "✅ Undervalued" if pe < mkt["PE_Industry"] else "⚠️ Premium",
                "✅" if 1 < pb < 4 else "⚠️",
                "✅ Cheap" if ev_ebitda < mkt["EV_EBITDA_Industry"] else "⚠️ Expensive",
                "✅" if ev_rev < 4 else "⚠️",
                "✅" if div_yield > 1 else "Low",
                "✅ Fair" if peg < 1.5 else "⚠️ Expensive"
            ]
        })
        st.dataframe(mv_df, use_container_width=True)

    st.info(f"""
**Quick Valuation Check:**
- P/E = {round(pe,2)}x vs Industry {mkt['PE_Industry']}x → {'Discount to peers ✅' if pe < mkt['PE_Industry'] else 'Premium to peers ⚠️'}
- EV/EBITDA = {round(ev_ebitda,2)}x vs Industry {mkt['EV_EBITDA_Industry']}x → {'Cheaper than peers ✅' if ev_ebitda < mkt['EV_EBITDA_Industry'] else 'Expensive vs peers ⚠️'}
- Intrinsic Value (Gordon Model P = D/(r-g)): ₹{round(dps/(0.12-growth_rate/100),2) if 0.12>growth_rate/100 else 'N/A (g≥r)'}
""")

# =========================================================
elif menu == "DuPont Analysis":
    st.header("🔬 DuPont Analysis — Decomposing ROE")
    st.markdown("""
## DuPont Framework

$$ROE = \\text{Net Margin} \\times \\text{Asset Turnover} \\times \\text{Financial Leverage}$$

**3-Factor DuPont:**
$$ROE = \\frac{PAT}{Revenue} \\times \\frac{Revenue}{Assets} \\times \\frac{Assets}{Equity}$$

**5-Factor DuPont:**
$$ROE = \\text{Tax Burden} \\times \\text{Interest Burden} \\times \\text{EBIT Margin} \\times \\text{Asset Turnover} \\times \\text{Leverage}$$
""")

    col1, col2 = st.columns(2)
    is_d = data["IS"]; bs = data["BS"]
    with col1:
        rev_d = st.number_input("Revenue (₹ Cr)", value=float(is_d["Revenue"]), key="dp_rev")
        pat_d = st.number_input("PAT (₹ Cr)", value=float(is_d["PAT"]), key="dp_pat")
        ebt_d = st.number_input("EBT (₹ Cr)", value=float(is_d["EBT"]))
        ebit_d = st.number_input("EBIT (₹ Cr)", value=float(is_d["EBIT"]), key="dp_ebit")
        assets_d = st.number_input("Total Assets (₹ Cr)", value=float(bs["Total_Assets"]), key="dp_a")
        equity_d = st.number_input("Total Equity (₹ Cr)", value=float(bs["Total_Equity"]), key="dp_eq")

    net_margin_d = pat_d/rev_d if rev_d>0 else 0
    asset_turn_d = rev_d/assets_d if assets_d>0 else 0
    leverage_d = assets_d/equity_d if equity_d>0 else 0
    roe_3f = net_margin_d * asset_turn_d * leverage_d * 100

    # 5-factor
    tax_burden = pat_d/ebt_d if ebt_d>0 else 0
    int_burden = ebt_d/ebit_d if ebit_d>0 else 0
    ebit_margin_d = ebit_d/rev_d if rev_d>0 else 0
    roe_5f = tax_burden * int_burden * ebit_margin_d * asset_turn_d * leverage_d * 100

    with col2:
        roe_actual = pat_d/equity_d*100 if equity_d>0 else 0
        st.metric("Actual ROE", pct(roe_actual))
        st.metric("3-Factor DuPont ROE", pct(roe_3f))
        st.metric("5-Factor DuPont ROE", pct(roe_5f))

    st.subheader("DuPont Decomposition Tree")
    dp_df = pd.DataFrame({
        "Driver": ["Net Profit Margin","Asset Turnover","Financial Leverage"],
        "Formula": ["PAT/Revenue","Revenue/Assets","Assets/Equity"],
        "Value": [pct(net_margin_d*100), f"{round(asset_turn_d,3)}x", f"{round(leverage_d,3)}x"],
        "ROE Contribution": [pct(net_margin_d*100), f"{round(asset_turn_d,3)}x × above", f"× {round(leverage_d,3)}x"]
    })
    st.table(dp_df)
    st.latex(f"ROE = {round(net_margin_d*100,2)}\\% \\times {round(asset_turn_d,3)}x \\times {round(leverage_d,3)}x = {round(roe_3f,2)}\\%")

    st.subheader("How to Improve ROE?")
    col1, col2, col3 = st.columns(3)
    col1.info(f"**Improve Margin ({pct(net_margin_d*100)})**\n- Cut costs / raise prices\n- Improve product mix\n- Reduce interest burden\n- Tax planning")
    col2.warning(f"**Improve Asset Turnover ({round(asset_turn_d,3)}x)**\n- Better capacity utilisation\n- Reduce idle assets\n- Improve working capital\n- Asset-light model")
    col3.success(f"**Use Leverage ({round(leverage_d,3)}x)**\n- Raise more debt (if D/E safe)\n- But increases financial risk\n- Works only if ROA > cost of debt")

    # Benchmark comparison
    st.subheader("DuPont — Peer Comparison")
    peer_data = {
        "Company": [data["name"], "Peer A (High Margin)", "Peer B (High Turnover)", "Peer C (Leveraged)"],
        "Net Margin %": [round(net_margin_d*100,2), 18.0, 8.0, 12.0],
        "Asset Turnover x": [round(asset_turn_d,3), 0.7, 1.8, 0.9],
        "Leverage x": [round(leverage_d,3), 1.8, 2.0, 3.5],
    }
    peer_df = pd.DataFrame(peer_data)
    peer_df["ROE %"] = peer_df["Net Margin %"] * peer_df["Asset Turnover x"] * peer_df["Leverage x"]
    peer_df["ROE %"] = peer_df["ROE %"].round(2)
    st.dataframe(peer_df, use_container_width=True)

# =========================================================
elif menu == "Cash Flow Quality & Earnings Quality":
    st.header("💎 Cash Flow Quality & Earnings Quality")
    st.markdown("""
## Why Does Earnings Quality Matter?

**High earnings quality** = PAT backed by actual cash; not by accounting choices.

**Low earnings quality** = PAT inflated by aggressive accounting; actual cash flow much lower.

## Key Quality Metrics

| Metric | Formula | Good Sign |
|---|---|---|
| **CFO/PAT Ratio** | Operating CF / Net Profit | > 1.0 (cash > accruals) |
| **Accrual Ratio** | (PAT - CFO) / Avg Total Assets | < 5% (low accruals) |
| **FCF Yield** | FCF / Market Cap | > 3-4% |
| **FCF/PAT** | Free Cash Flow / PAT | > 0.8 |
| **Earnings Persistence** | Consistent PAT growth | Smooth, not lumpy |
""")

    col1, col2 = st.columns(2)
    with col1:
        pat_eq = st.number_input("PAT / Net Income (₹ Cr)", value=float(data["IS"]["PAT"]))
        cfo_eq = st.number_input("Operating Cash Flow (₹ Cr)", value=164.0)
        capex_eq = st.number_input("Capital Expenditure (₹ Cr)", value=90.0)
        avg_assets = st.number_input("Avg Total Assets (₹ Cr)", value=1206.5)
        mktcap_eq = st.number_input("Market Cap (₹ Cr)", value=float(data["Market"]["Share_Price"]*data["IS"]["Shares"]))
    with col2:
        fcf_eq = cfo_eq - capex_eq
        cfo_pat = cfo_eq/pat_eq if pat_eq>0 else 0
        accrual_ratio = (pat_eq - cfo_eq)/avg_assets*100 if avg_assets>0 else 0
        fcf_yield = fcf_eq/mktcap_eq*100 if mktcap_eq>0 else 0
        fcf_pat = fcf_eq/pat_eq if pat_eq>0 else 0

        eq_df = pd.DataFrame({
            "Metric": ["CFO/PAT Ratio","Accrual Ratio","Free Cash Flow","FCF/PAT","FCF Yield"],
            "Value": [times(cfo_pat), pct(accrual_ratio), cr(fcf_eq), times(fcf_pat), pct(fcf_yield)],
            "Green Zone": [">1.0x","<5%","Positive",">0.8x",">3%"],
            "Quality": [
                "✅ High" if cfo_pat > 1.0 else "⚠️ Low",
                "✅ Low accruals" if abs(accrual_ratio) < 5 else "⚠️ High accruals",
                "✅" if fcf_eq > 0 else "❌",
                "✅" if fcf_pat > 0.8 else "⚠️",
                "✅" if fcf_yield > 3 else "⚠️"
            ]
        })
        st.dataframe(eq_df, use_container_width=True)

    st.subheader("5 Signs of High Earnings Quality")
    signs = [
        ("CFO > PAT consistently", "Operating cash consistently exceeds reported profits"),
        ("Receivables growing slower than Revenue", "No stuffing of channel; collections are healthy"),
        ("Low and stable accruals", "Accounting choices not inflating earnings"),
        ("Stable/improving gross margin", "Core business healthy; not cost-cutting to show profits"),
        ("FCF positive and growing", "Business is truly generating cash for shareholders"),
    ]
    for sign, desc in signs:
        st.success(f"✅ **{sign}:** {desc}")

# =========================================================
elif menu == "Working Capital Analysis":
    st.header("📦 Working Capital Analysis")
    st.markdown("""
## Working Capital = Current Assets − Current Liabilities

**Gross Working Capital (GWC)** = Total Current Assets

**Net Working Capital (NWC)** = Current Assets − Current Liabilities

**Operating Working Capital (OWC)** = Debtors + Inventory − Trade Payables
""")

    col1, col2 = st.columns(2)
    bs = data["BS"]; is_d = data["IS"]
    with col1:
        cash_wc = st.number_input("Cash & Equivalents (₹ Cr)", value=float(bs["Cash"]), key="wc_cash")
        debtors_wc = st.number_input("Trade Receivables (₹ Cr)", value=float(bs["Debtors"]), key="wc_deb")
        inv_wc = st.number_input("Inventory (₹ Cr)", value=float(bs["Inventory"]), key="wc_inv")
        other_ca_wc = st.number_input("Other Current Assets (₹ Cr)", value=float(bs["Other_CA"]), key="wc_oca")
        creditors_wc = st.number_input("Trade Payables (₹ Cr)", value=float(bs["Creditors"]), key="wc_cred")
        short_debt_wc = st.number_input("Short-term Debt (₹ Cr)", value=float(bs["Short_Debt"]), key="wc_sd")
        other_cl_wc = st.number_input("Other Current Liabilities (₹ Cr)", value=float(bs["Other_CL"]), key="wc_ocl")
        rev_wc = st.number_input("Revenue (₹ Cr)", value=float(is_d["Revenue"]), key="wc_rev")
        cogs_wc = st.number_input("COGS (₹ Cr)", value=float(is_d["COGS"]), key="wc_cogs")

    total_ca_wc = cash_wc + debtors_wc + inv_wc + other_ca_wc
    total_cl_wc = creditors_wc + short_debt_wc + other_cl_wc
    gwc = total_ca_wc
    nwc = total_ca_wc - total_cl_wc
    owc = debtors_wc + inv_wc - creditors_wc

    dso_wc = debtors_wc/(rev_wc/365) if rev_wc>0 else 0
    dio_wc = inv_wc/(cogs_wc/365) if cogs_wc>0 else 0
    dpo_wc = creditors_wc/(cogs_wc/365) if cogs_wc>0 else 0
    ccc_wc = dso_wc + dio_wc - dpo_wc

    with col2:
        wc_df = pd.DataFrame({
            "Metric": ["Gross Working Capital","Net Working Capital","Operating WC",
                       "DSO","DIO","DPO","Cash Conversion Cycle"],
            "Value": [cr(gwc), cr(nwc), cr(owc),
                      f"{round(dso_wc,1)}d", f"{round(dio_wc,1)}d",
                      f"{round(dpo_wc,1)}d", f"{round(ccc_wc,1)}d"]
        })
        st.dataframe(wc_df, use_container_width=True)

    cash_freed = st.number_input("Target CCC reduction (days)", value=10.0)
    cash_release = rev_wc * cash_freed / 365
    st.metric(f"Cash freed by reducing CCC {cash_freed:.0f} days", cr(round(cash_release,2)))

# =========================================================
elif menu == "Trend Analysis":
    st.header("📈 Trend Analysis — Multi-Year Performance")

    years = ["FY20","FY21","FY22","FY23","FY24"]
    revenues = [700, 750, 900, 1000, 1200]
    pats = [50, 55, 80, 94, 144]
    roe_hist = [10.5, 10.8, 13.2, 18.7, 25.3]
    debt_ebitda_hist = [3.2, 2.9, 2.5, 2.2, 1.8]

    revenues = [st.sidebar.number_input(f"Revenue {y} (₹Cr)", value=float(r), key=f"trend_r_{y}")
                if False else r for r, y in zip(revenues, years)]

    col1, col2 = st.columns(2)
    with col1:
        fig1 = go.Figure()
        fig1.add_trace(go.Bar(x=years, y=revenues, name='Revenue', marker_color='#174EA6'))
        fig1.add_trace(go.Bar(x=years, y=pats, name='PAT', marker_color='#F5A623'))
        rev_cagr = (revenues[-1]/revenues[0])**(1/(len(years)-1))-1
        fig1.update_layout(barmode='group', title=f"Revenue & PAT Trend (Rev CAGR: {pct(rev_cagr*100)})")
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=years, y=roe_hist, mode='lines+markers',
                                   name='ROE%', line=dict(color='green', width=2)))
        fig2.add_trace(go.Scatter(x=years, y=debt_ebitda_hist, mode='lines+markers',
                                   name='Debt/EBITDA', line=dict(color='red', width=2, dash='dash'),
                                   yaxis='y2'))
        fig2.update_layout(title="ROE vs Leverage Trend",
                           yaxis2=dict(overlaying='y', side='right'))
        st.plotly_chart(fig2, use_container_width=True)

    st.subheader("Margin Trend")
    gross_margins = [32, 33, 35, 38, 40]
    ebitda_margins = [20, 18, 22, 22, 25]
    net_margins = [7.1, 7.3, 8.9, 9.4, 12.0]

    fig3 = go.Figure()
    for margins, name, color in [(gross_margins,'Gross Margin','green'),
                                   (ebitda_margins,'EBITDA Margin','blue'),
                                   (net_margins,'Net Margin','orange')]:
        fig3.add_trace(go.Scatter(x=years, y=margins, mode='lines+markers',
                                   name=name, line=dict(color=color, width=2)))
    fig3.update_layout(title="Margin Trend (5 Years)", yaxis_title="%")
    st.plotly_chart(fig3, use_container_width=True)

    trend_conclusion = "expanding" if net_margins[-1] > net_margins[0] else "contracting"
    st.success(f"**Trend:** Margins are **{trend_conclusion}** over 5 years. Revenue CAGR = {pct(rev_cagr*100)}.")

# =========================================================
elif menu == "Inter-Firm Comparison":
    st.header("🏆 Inter-Firm Comparison (Benchmarking)")

    st.subheader("Compare Your Company vs Industry Peers")
    companies = {
        data["name"]: {"Revenue":1200,"EBITDA Margin":25,"Net Margin":12,"ROE":25.3,
                        "DE":0.84,"ICR":5.0,"PE":19.4,"Asset_Turn":0.96},
        "Peer Alpha Ltd": {"Revenue":2000,"EBITDA Margin":22,"Net Margin":10,"ROE":18.5,
                            "DE":1.1,"ICR":4.2,"PE":24,"Asset_Turn":1.0},
        "Peer Beta Corp": {"Revenue":800,"EBITDA Margin":28,"Net Margin":14,"ROE":22,
                            "DE":0.5,"ICR":8,"PE":32,"Asset_Turn":0.75},
        "Industry Median": {"Revenue":1100,"EBITDA Margin":22,"Net Margin":11,"ROE":20,
                             "DE":0.9,"ICR":5,"PE":22,"Asset_Turn":0.9},
    }

    comp_df = pd.DataFrame(companies).T.reset_index()
    comp_df.columns = ["Company","Revenue","EBITDA Margin%","Net Margin%","ROE%","D/E","ICR","P/E","Asset Turnover"]
    st.dataframe(comp_df, use_container_width=True)

    metric_to_plot = st.selectbox("Visualise Metric", ["EBITDA Margin%","Net Margin%","ROE%","D/E","P/E"])
    fig = go.Figure(go.Bar(
        x=comp_df["Company"],
        y=comp_df[metric_to_plot],
        marker_color=['#F5A623' if c == data["name"] else '#174EA6' for c in comp_df["Company"]]
    ))
    fig.update_layout(title=f"{metric_to_plot} — Peer Comparison", yaxis_title=metric_to_plot)
    st.plotly_chart(fig, use_container_width=True)

# =========================================================
elif menu == "Red Flags & Creative Accounting":
    st.header("🚩 Red Flags & Creative Accounting")
    st.markdown("""
## Red Flags in Financial Statements — What to Watch For

**Creative accounting** uses flexibility in accounting standards to make
financials look better than reality. It is legal (unlike fraud) but misleading.
""")

    red_flags = {
        "Revenue Manipulation": [
            "Revenue growing much faster than cash collections (DSO rising sharply)",
            "Channel stuffing — shipping goods to distributors just before year-end",
            "Bill-and-hold arrangements — revenue recognised before delivery",
            "Related party sales at inflated prices",
            "Revenue growth inconsistent with industry trends",
        ],
        "Cost Manipulation": [
            "Capitalising operating expenses (increases assets, reduces costs)",
            "Changing depreciation method to reduce depreciation charge",
            "Aggressive inventory valuation (FIFO vs LIFO in different periods)",
            "Underprovisioning for doubtful debts / warranty claims",
            "Deferring expenses to future periods",
        ],
        "Balance Sheet Manipulation": [
            "Goodwill impairment not taken when clearly warranted",
            "Off-balance-sheet entities (SPVs) hiding liabilities",
            "Operating leases kept off balance sheet (pre-Ind AS 116)",
            "Pledging promoter shares (often a liquidity signal)",
            "Inventory write-offs or write-ups to manipulate gross margin",
        ],
        "Cash Flow Red Flags": [
            "CFO consistently < PAT (accrual-based earnings not converting to cash)",
            "Rising accounts receivable as % of revenue (stuffing)",
            "Large 'other operating adjustments' not explained",
            "Capex classified as investment (to boost CFO artificially)",
            "Consistently negative FCF despite reported profits",
        ],
        "Auditor/Disclosure Red Flags": [
            "Auditor resignation or frequent auditor change",
            "Qualified audit opinion or emphasis of matter",
            "Restatement of prior year financials",
            "Promoter pledging > 50% of holdings",
            "Delay in filing quarterly results",
        ],
    }

    for category, flags in red_flags.items():
        with st.expander(f"🚩 {category}"):
            for flag in flags:
                st.warning(f"⚠️ {flag}")

    st.subheader("🔢 Red Flag Scorecard")
    st.markdown("Rate your company on the following (1=No concern, 5=Major red flag):")
    col1, col2 = st.columns(2)
    scores = []
    with col1:
        s1 = st.slider("CFO/PAT ratio < 0.8 consistently", 1, 5, 1)
        s2 = st.slider("Receivables growing faster than Revenue", 1, 5, 2)
        s3 = st.slider("Promoter pledging > 30% of shares", 1, 5, 1)
        s4 = st.slider("Auditor change/qualified opinion", 1, 5, 1)
        scores = [s1, s2, s3, s4]
    with col2:
        s5 = st.slider("Related party transactions > 20% of Revenue", 1, 5, 1)
        s6 = st.slider("Frequent restatements/adjustments", 1, 5, 1)
        s7 = st.slider("FCF negative despite reported profits", 1, 5, 1)
        s8 = st.slider("Debt/EBITDA > 4x", 1, 5, 2)
        scores += [s5, s6, s7, s8]

    total_rf_score = sum(scores)
    max_rf = len(scores)*5
    if total_rf_score/max_rf > 0.6:
        st.error(f"🚩 HIGH RISK: Score {total_rf_score}/{max_rf}. Multiple red flags present. Investigate further.")
    elif total_rf_score/max_rf > 0.4:
        st.warning(f"⚠️ MODERATE RISK: Score {total_rf_score}/{max_rf}. Some concerns — monitor closely.")
    else:
        st.success(f"✅ LOW RISK: Score {total_rf_score}/{max_rf}. No major red flags detected.")

# =========================================================
elif menu == "Credit Analysis (Banker's View)":
    st.header("🏦 Credit Analysis — The Banker's Perspective")
    st.markdown("""
## 5C's of Credit Analysis

| C | What to Assess | Key Question |
|---|---|---|
| **Character** | Management quality, track record, governance | Do they have a history of honouring obligations? |
| **Capacity** | Ability to repay from operations | Can cashflows service the debt? |
| **Capital** | Own funds invested | Is promoter committed (skin in the game)? |
| **Collateral** | Security/assets pledged | What can we recover if they default? |
| **Conditions** | Industry outlook, macro | Will the business continue to operate? |
""")

    col1, col2 = st.columns(2)
    is_d = data["IS"]; bs = data["BS"]
    with col1:
        loan_amount = st.number_input("Proposed Loan Amount (₹ Cr)", value=200.0)
        loan_rate = st.number_input("Interest Rate (%)", value=10.5)
        tenure = st.number_input("Loan Tenure (years)", value=5)
        ebit_ca = st.number_input("EBIT (₹ Cr)", value=float(is_d["EBIT"]))
        existing_interest = st.number_input("Existing Interest Expense (₹ Cr)", value=float(is_d["Interest"]))
        total_d_ca = st.number_input("Existing Total Debt (₹ Cr)", value=float(bs["Short_Debt"]+bs["Long_Debt"]))
        equity_ca = st.number_input("Total Equity (₹ Cr)", value=float(bs["Total_Equity"]))
        ebitda_ca = st.number_input("EBITDA (₹ Cr)", value=float(is_d["EBITDA"]))
        cfo_ca = st.number_input("Operating Cash Flow (₹ Cr)", value=164.0)
        collateral_val = st.number_input("Collateral Value (₹ Cr)", value=350.0)

    new_interest = loan_amount * loan_rate/100
    total_interest = existing_interest + new_interest
    new_total_debt = total_d_ca + loan_amount
    new_de = new_total_debt/equity_ca if equity_ca>0 else 0
    new_icr = ebit_ca/total_interest if total_interest>0 else 0
    new_debt_ebitda = new_total_debt/ebitda_ca if ebitda_ca>0 else 0
    annual_repayment = loan_amount/tenure
    total_debt_service = total_interest + annual_repayment
    dscr_ca = cfo_ca/total_debt_service if total_debt_service>0 else 0
    security_cover = collateral_val/loan_amount if loan_amount>0 else 0

    with col2:
        ca_df = pd.DataFrame({
            "Credit Metric": ["New D/E Ratio","Interest Coverage (ICR)","Debt/EBITDA","DSCR","Security Cover"],
            "Value": [times(new_de), times(new_icr), times(new_debt_ebitda),
                      times(dscr_ca), times(security_cover)],
            "Minimum Threshold": ["<1.5x",">3x","<3x",">1.25x",">1.5x"],
            "Decision": [
                "✅ Acceptable" if new_de<1.5 else "❌ Too high",
                "✅ Safe" if new_icr>3 else ("⚠️ Marginal" if new_icr>1.5 else "❌ Reject"),
                "✅ Comfortable" if new_debt_ebitda<3 else "❌ High leverage",
                "✅ Adequate" if dscr_ca>1.25 else "❌ Insufficient",
                "✅ Adequate" if security_cover>1.5 else "⚠️ Borderline"
            ]
        })
        st.dataframe(ca_df, use_container_width=True)

    passed = sum(1 for v in ca_df["Decision"] if "✅" in v)
    if passed >= 4:
        st.success(f"✅ **RECOMMEND SANCTION** — {passed}/5 credit metrics pass. Proceed with standard terms.")
    elif passed >= 3:
        st.warning(f"⚠️ **CONDITIONAL SANCTION** — {passed}/5 pass. Additional collateral or covenants required.")
    else:
        st.error(f"❌ **DECLINE** — Only {passed}/5 credit metrics pass. Credit risk too high.")

# =========================================================
elif menu == "Equity Valuation from Financials":
    st.header("💹 Equity Valuation from Financial Statements")
    st.markdown("""
## Approaches to Equity Valuation

| Method | Formula | Use Case |
|---|---|---|
| **P/E Multiple** | Industry P/E × EPS | Listed companies with stable earnings |
| **EV/EBITDA** | Industry multiple × EBITDA − Net Debt | Capital structure agnostic |
| **Gordon Growth (DDM)** | D₁ / (Ke − g) | Dividend-paying mature companies |
| **DCF** | Sum of PV(FCF) + Terminal Value | Most rigorous; needs projections |
| **P/BV** | Industry P/B × Book Value per share | Banks, asset-heavy firms |
""")

    col1, col2 = st.columns(2)
    is_d = data["IS"]; bs = data["BS"]; mkt = data["Market"]
    with col1:
        eps_val = st.number_input("EPS (₹)", value=float(is_d["EPS"]))
        dps_val = st.number_input("Dividend Per Share (₹)", value=3.0)
        bvps_val = st.number_input("Book Value Per Share (₹)", value=float(bs["Total_Equity"]*1e7/(is_d["Shares"]*1e7)))
        pe_ind = st.number_input("Industry P/E", value=float(mkt["PE_Industry"]))
        ev_ebitda_ind = st.number_input("Industry EV/EBITDA", value=float(mkt["EV_EBITDA_Industry"]))
        pb_ind = st.number_input("Industry P/B", value=3.5)
        ke = st.number_input("Cost of Equity Ke (%)", value=12.0)
        g = st.number_input("Dividend Growth Rate g (%)", value=8.0)
        ebitda_val = st.number_input("EBITDA (₹ Cr)", value=float(is_d["EBITDA"]), key="val_ebitda")
        net_debt_val = st.number_input("Net Debt (₹ Cr)", value=float(bs["Short_Debt"]+bs["Long_Debt"]-bs["Cash"]))
        shares_val = st.number_input("Shares (Cr)", value=float(is_d["Shares"]), key="val_shares")

    pe_value = pe_ind * eps_val
    ev = ev_ebitda_ind * ebitda_val
    ev_per_share_val = (ev - net_debt_val) * 1e7 / (shares_val * 1e7)
    ddm_value = dps_val * (1+g/100) / ((ke-g)/100) if ke > g else float('nan')
    pb_value = pb_ind * bvps_val

    with col2:
        val_df = pd.DataFrame({
            "Method": ["P/E Multiple","EV/EBITDA Method","Gordon Growth (DDM)","P/B Multiple"],
            "Intrinsic Value (₹/share)": [round(pe_value,2),
                                           round(ev_per_share_val,2) if ev_per_share_val>0 else "—",
                                           round(ddm_value,2) if not np.isnan(ddm_value) else "N/A (g≥Ke)",
                                           round(pb_value,2)],
        })
        st.dataframe(val_df, use_container_width=True)

        valid_vals = [v for v in [pe_value, ev_per_share_val, pb_value]
                      if isinstance(v, float) and v > 0]
        if not np.isnan(ddm_value): valid_vals.append(ddm_value)
        avg_intrinsic = np.mean(valid_vals) if valid_vals else 0

        st.metric("Average Intrinsic Value", f"₹{round(avg_intrinsic,2)}")
        st.metric("Current Market Price", f"₹{mkt['Share_Price']}")
        upside = (avg_intrinsic - mkt["Share_Price"])/mkt["Share_Price"]*100
        if upside > 15:
            st.success(f"✅ Undervalued! Upside potential = {pct(upside)}")
        elif upside < -15:
            st.error(f"❌ Overvalued! Downside risk = {pct(abs(upside))}")
        else:
            st.info(f"Fair value range. Upside/downside = {pct(upside)}")

# =========================================================
elif menu == "Integrated Decision Framework":
    st.header("🎯 Integrated FSA Decision Framework")
    st.markdown("""
## The COMPLETE Decision Framework for Future-Ready Managers

Use this framework to make ONE clear recommendation: **Buy / Hold / Sell / Lend / Partner**
""")

    st.subheader("📊 Complete Scorecard")
    categories_score = {
        "Profitability": {"metrics": ["Gross Margin>30%","EBITDA Margin>18%","Net Margin>10%","ROE>15%"], "weights": [25,25,25,25]},
        "Liquidity": {"metrics": ["CR>1.5x","QR>1.0x","CCC<60d","CFO>PAT"], "weights": [25,25,25,25]},
        "Solvency": {"metrics": ["D/E<1.5x","ICR>3x","Debt/EBITDA<3x","DSCR>1.25x"], "weights": [25,25,25,25]},
        "Efficiency": {"metrics": ["Asset Turn>0.9x","Inv Turn improving","DSO<45d","Asset quality"], "weights": [25,25,25,25]},
        "Valuation": {"metrics": ["P/E vs Industry","EV/EBITDA vs peers","FCF Yield>3%","PEG<1.5x"], "weights": [25,25,25,25]},
        "Quality": {"metrics": ["CFO/PAT>1x","Accruals low","No red flags","Earnings consistent"], "weights": [25,25,25,25]},
    }

    col1, col2 = st.columns(2)
    total_weighted = 0
    scores_idf = {}
    with col1:
        for cat, details in list(categories_score.items())[:3]:
            st.markdown(f"**{cat}** (rate 1-10)")
            cat_score = st.slider(cat, 1, 10, 7, key=f"idf_{cat}")
            scores_idf[cat] = cat_score
    with col2:
        for cat, details in list(categories_score.items())[3:]:
            st.markdown(f"**{cat}** (rate 1-10)")
            cat_score = st.slider(cat, 1, 10, 7, key=f"idf_{cat}")
            scores_idf[cat] = cat_score

    overall = np.mean(list(scores_idf.values()))
    fig = go.Figure(go.Scatterpolar(
        r=list(scores_idf.values()),
        theta=list(scores_idf.keys()),
        fill='toself', line=dict(color='#174EA6')
    ))
    fig.update_layout(polar=dict(radialaxis=dict(range=[0,10])),
                       title="Company Score Card — Spider Chart", height=380)
    st.plotly_chart(fig, use_container_width=True)

    st.metric("Overall Score", f"{round(overall,1)}/10")
    if overall >= 7.5:
        st.success("✅ **STRONG BUY / SAFE LEND** — Company scores well across all dimensions")
    elif overall >= 6.0:
        st.info("📊 **HOLD / CAUTIOUS BUY** — Mostly positive but some areas need monitoring")
    elif overall >= 4.5:
        st.warning("⚠️ **WATCH / CONDITIONAL LEND** — Material concerns in 2+ areas")
    else:
        st.error("❌ **AVOID / DO NOT LEND** — Multiple serious concerns identified")

    st.subheader("One-Page Decision Summary")
    decision_text = st.text_area("Write your investment/lending recommendation (3-5 sentences):",
                                  placeholder="Based on the analysis, [Company] shows [strengths]. Key concerns are [risks]. We recommend [Buy/Hold/Sell/Lend] because...")
    if decision_text:
        st.success(f"Your recommendation documented: {decision_text[:100]}...")

# =========================================================
elif menu == "Step-by-Step Solver":
    st.header("🧠 Step-by-Step Solver")
    problem = st.selectbox("Choose Problem", [
        "Current Ratio",
        "DuPont ROE (3-factor)",
        "EPS Calculation",
        "DIO / DSO / DPO / CCC",
        "Interest Coverage Ratio",
        "EV/EBITDA Valuation",
        "D/E Ratio",
        "FCF Calculation",
    ])

    if problem == "Current Ratio":
        ca=st.number_input("Current Assets",value=450.0); cl=st.number_input("Current Liabilities",value=230.0)
        st.write("**CR = CA / CL**")
        st.latex(f"= {ca}/{cl} = {round(ca/cl,4)}x")
        st.success(f"Current Ratio = {round(ca/cl,4)}x {'✅' if ca/cl>=1.5 else '⚠️'}")

    elif problem == "DuPont ROE (3-factor)":
        pat=st.number_input("PAT",value=144.0); rev=st.number_input("Revenue",value=1200.0)
        assets=st.number_input("Total Assets",value=1250.0); eq=st.number_input("Equity",value=570.0)
        nm=pat/rev; at=rev/assets; lev=assets/eq
        roe=nm*at*lev*100
        st.write("**ROE = Net Margin × Asset Turnover × Leverage**")
        st.latex(f"= {round(nm*100,2)}\\% \\times {round(at,4)}x \\times {round(lev,4)}x = {round(roe,4)}\\%")

    elif problem == "DIO / DSO / DPO / CCC":
        inv=st.number_input("Inventory",value=150.0); cogs=st.number_input("COGS",value=720.0)
        deb=st.number_input("Debtors",value=200.0); rev=st.number_input("Revenue",value=1200.0)
        cred=st.number_input("Creditors",value=120.0)
        dio=inv/(cogs/365); dso=deb/(rev/365); dpo=cred/(cogs/365); ccc=dio+dso-dpo
        st.latex(f"DIO = {inv}/({cogs}/365) = {round(dio,1)} \\text{{ days}}")
        st.latex(f"DSO = {deb}/({rev}/365) = {round(dso,1)} \\text{{ days}}")
        st.latex(f"DPO = {cred}/({cogs}/365) = {round(dpo,1)} \\text{{ days}}")
        st.success(f"CCC = {round(dio,1)} + {round(dso,1)} − {round(dpo,1)} = {round(ccc,1)} days")

    elif problem == "EPS Calculation":
        pat=st.number_input("PAT (₹ Cr)",value=144.0); shares=st.number_input("Shares (Cr)",value=10.0)
        pref_div=st.number_input("Preference Dividend (₹ Cr)",value=0.0)
        eps=(pat-pref_div)/shares*1e7/1e7
        st.write("**EPS = (PAT - Pref Dividend) / Shares**")
        st.latex(f"= ({pat}-{pref_div})/{shares} = ₹{round(eps,2)}")
        st.success(f"EPS = ₹{round(eps,2)} per share")

    elif problem == "Interest Coverage Ratio":
        ebit=st.number_input("EBIT",value=240.0); interest=st.number_input("Interest",value=48.0)
        icr=ebit/interest if interest>0 else 0
        st.write("**ICR = EBIT / Interest**")
        st.latex(f"= {ebit}/{interest} = {round(icr,4)}x")
        st.success(f"ICR = {round(icr,4)}x {'✅ Safe' if icr>3 else '⚠️ Low'}")

    elif problem == "EV/EBITDA Valuation":
        ebitda=st.number_input("EBITDA (₹ Cr)",value=300.0); ev_mult=st.number_input("EV/EBITDA Multiple",value=14.0)
        net_d=st.number_input("Net Debt (₹ Cr)",value=370.0); shares=st.number_input("Shares (Cr)",value=10.0)
        ev=ebitda*ev_mult; equity_val=(ev-net_d); val_per_share=equity_val/shares*1e7/1e7
        st.latex(f"EV = {ebitda} \\times {ev_mult} = {round(ev,2)} Cr")
        st.latex(f"\\text{{Equity Value}} = {round(ev,2)} - {net_d} = {round(equity_val,2)} Cr")
        st.success(f"Intrinsic Value per share = ₹{round(val_per_share*1e7/1e7,2)}")

    elif problem == "D/E Ratio":
        td=st.number_input("Total Debt",value=480.0); eq=st.number_input("Equity",value=570.0)
        de=td/eq if eq>0 else 0
        st.write("**D/E = Total Debt / Total Equity**")
        st.latex(f"= {td}/{eq} = {round(de,4)}x")
        st.success(f"D/E = {round(de,4)}x {'✅' if de<1.5 else '⚠️'}")

    elif problem == "FCF Calculation":
        cfo=st.number_input("Operating Cash Flow (CFO)",value=164.0)
        capex=st.number_input("Capital Expenditure (CapEx)",value=90.0)
        fcf=cfo-capex
        st.write("**FCF = CFO − CapEx**")
        st.latex(f"= {cfo} - {capex} = {round(fcf,2)}")
        st.success(f"Free Cash Flow = ₹{round(fcf,2)} Cr {'✅' if fcf>0 else '❌'}")

# =========================================================
elif menu == "AI Hint System":
    st.header("🤖 AI Hint System")
    problems_h = {
        "Current Ratio": {"q":"CA=₹450Cr, CL=₹230Cr. Find Current Ratio.",
            "correct":450/230,"hints":["CR = CA / CL","= 450/230"],"formula":r"CR = 450/230 = 1.96x"},
        "Gross Margin": {"q":"Revenue=₹1200Cr, COGS=₹720Cr. Find Gross Margin %.",
            "correct":(1200-720)/1200*100,"hints":["Gross Margin = (Revenue-COGS)/Revenue × 100","= (1200-720)/1200 × 100"],"formula":r"= 480/1200 \times 100 = 40\%"},
        "ROE (DuPont)": {"q":"Net Margin=12%, Asset Turnover=0.96x, Leverage=2.19x. Find ROE.",
            "correct":12*0.96*2.19,"hints":["ROE = NM × AT × Leverage","= 12% × 0.96 × 2.19"],"formula":r"= 12 \times 0.96 \times 2.19 = 25.2\%"},
    }
    sel=st.selectbox("Choose Problem",list(problems_h.keys()))
    prob=problems_h[sel]
    st.markdown(f"**Problem:** {prob['q']}")
    ans=st.number_input("Your Answer",value=0.0,key="fsa_hint_ans")
    if st.button("Check"):
        if abs(ans-prob["correct"])<abs(prob["correct"])*0.02+0.01:
            st.success(f"✅ Correct! = {round(prob['correct'],4)}")
            st.balloons()
        else: st.error("❌ Use hints below.")
    for i,h in enumerate(prob["hints"],1):
        if st.checkbox(f"Hint {i}",key=f"fsah_{sel}_{i}"): st.info(f"💡 {h}")
    if st.checkbox("Show Solution",key=f"fsas_{sel}"): st.latex(prob["formula"])

# =========================================================
elif menu == "Quiz Engine":
    st.header("📝 FSA Quiz Engine")
    difficulty=st.selectbox("Difficulty",["Beginner","Intermediate","Advanced"])
    if "fsa_quiz_gen" not in st.session_state or st.button("🔄 New Question"):
        if difficulty=="Beginner":
            st.session_state.fsa_ca=random.choice([300,400,500,600])
            st.session_state.fsa_cl=random.choice([150,200,250,300])
            st.session_state.fsa_qtype="cr"
        elif difficulty=="Intermediate":
            st.session_state.fsa_pat=random.choice([100,120,150,200])
            st.session_state.fsa_rev=random.choice([800,1000,1200,1500])
            st.session_state.fsa_assets=random.choice([1000,1200,1500,2000])
            st.session_state.fsa_equity=random.choice([400,500,600,700])
            st.session_state.fsa_qtype="dupont"
        else:
            st.session_state.fsa_inv=random.choice([100,150,200])
            st.session_state.fsa_cogs=random.choice([500,600,700,800])
            st.session_state.fsa_deb=random.choice([150,200,250])
            st.session_state.fsa_rev=random.choice([800,1000,1200])
            st.session_state.fsa_cred=random.choice([80,100,120])
            st.session_state.fsa_qtype="ccc"
        st.session_state.fsa_quiz_gen=True

    qtype=st.session_state.fsa_qtype
    if qtype=="cr":
        ca=st.session_state.fsa_ca; cl=st.session_state.fsa_cl
        correct=ca/cl
        st.markdown(f"**Current Ratio:** CA=₹{ca}Cr, CL=₹{cl}Cr")
    elif qtype=="dupont":
        pat=st.session_state.fsa_pat; rev=st.session_state.fsa_rev
        assets=st.session_state.fsa_assets; eq=st.session_state.fsa_equity
        correct=(pat/rev)*(rev/assets)*(assets/eq)*100
        st.markdown(f"**DuPont ROE (%):** PAT=₹{pat}Cr, Revenue=₹{rev}Cr, Assets=₹{assets}Cr, Equity=₹{eq}Cr")
    else:
        inv=st.session_state.fsa_inv; cogs=st.session_state.fsa_cogs
        deb=st.session_state.fsa_deb; rev=st.session_state.fsa_rev
        cred=st.session_state.fsa_cred
        dio=inv/(cogs/365); dso=deb/(rev/365); dpo=cred/(cogs/365)
        correct=dio+dso-dpo
        st.markdown(f"**Cash Conversion Cycle (days):**\nInventory=₹{inv}Cr, COGS=₹{cogs}Cr, Debtors=₹{deb}Cr, Revenue=₹{rev}Cr, Creditors=₹{cred}Cr")

    ans=st.number_input("Your Answer",value=0.0,key="fsa_quiz_ans")
    if st.button("Submit"):
        if abs(ans-correct)<max(0.05,abs(correct)*0.02):
            st.success(f"✅ Correct! = {round(correct,4)}")
            st.balloons()
        else: st.error(f"❌ Answer = {round(correct,4)}")

# =========================================================
elif menu == "Excel Formula Trainer":
    st.header("📊 Excel Formula Trainer — Financial Ratios")
    problems_ex = {
        "Gross Margin %":{"desc":"Revenue=B2, COGS=B3","fn":"=","answer":"=(B2-B3)/B2*100","hint":"=(Revenue-COGS)/Revenue*100"},
        "Current Ratio":{"desc":"CA=B10, CL=B15","fn":"=","answer":"=B10/B15","hint":"=CA/CL"},
        "D/E Ratio":{"desc":"Total Debt=B20, Equity=B25","fn":"=","answer":"=B20/B25","hint":"=Total_Debt/Equity"},
        "ICR":{"desc":"EBIT=B5, Interest=B8","fn":"=","answer":"=B5/B8","hint":"=EBIT/Interest"},
        "ROE":{"desc":"PAT=B4, Equity=B25","fn":"=","answer":"=B4/B25*100","hint":"=PAT/Equity*100"},
        "EPS":{"desc":"PAT=B4 (Cr), Shares=B30 (Cr)","fn":"=","answer":"=B4/B30","hint":"=PAT/Shares (both in same unit)"},
        "P/E Ratio":{"desc":"Price=B35, EPS=B36","fn":"=","answer":"=B35/B36","hint":"=Market_Price/EPS"},
        "DIO (days)":{"desc":"Inventory=B11, COGS=B3","fn":"=","answer":"=B11/(B3/365)","hint":"=Inventory/(COGS/365)"},
        "FCF":{"desc":"CFO=B40, CapEx=B41 (negative)","fn":"=","answer":"=B40+B41","hint":"=CFO+CapEx (CapEx is negative)"},
        "EV/EBITDA":{"desc":"Market Cap=B50, Debt=B51, Cash=B52, EBITDA=B53","fn":"=","answer":"=(B50+B51-B52)/B53","hint":"=(MktCap+Debt-Cash)/EBITDA"},
    }
    sel=st.selectbox("Choose Ratio",list(problems_ex.keys()))
    prob=problems_ex[sel]
    st.markdown(f"**Formula for:** {sel} | Inputs: {prob['desc']}")
    st.info(f"💡 Hint: `{prob['hint']}`")
    user_inp=st.text_input("Enter Excel Formula")
    if st.button("Validate"):
        if user_inp.startswith("="):
            st.success(f"✅ Reference: `{prob['answer']}`")
        else: st.error("Start with =")
    if st.checkbox("Show Answer"): st.code(prob["answer"],language="excel")

# =========================================================
elif menu == "Formula Cheat Sheet":
    st.header("📘 FSA Formula Cheat Sheet")
    formulas="""
FINANCIAL STATEMENT ANALYSIS — COMPLETE FORMULA REFERENCE
=============================================================

INCOME STATEMENT
──────────────────────────────────────────────────────────
Gross Profit = Revenue - COGS
EBITDA = Gross Profit - Operating Expenses
EBIT = EBITDA - Depreciation
EBT = EBIT - Interest
PAT = EBT × (1 - Tax Rate)
EPS = PAT / Number of Shares

PROFITABILITY RATIOS
──────────────────────────────────────────────────────────
Gross Margin = Gross Profit / Revenue × 100
EBITDA Margin = EBITDA / Revenue × 100
EBIT Margin = EBIT / Revenue × 100
Net Profit Margin = PAT / Revenue × 100
ROE = PAT / Equity × 100
ROA = PAT / Total Assets × 100
ROCE = EBIT / Capital Employed × 100
  [Capital Employed = Equity + Long-term Debt]

DUPONT ANALYSIS
──────────────────────────────────────────────────────────
ROE (3-factor) = Net Margin × Asset Turnover × Leverage
= (PAT/Rev) × (Rev/Assets) × (Assets/Equity)

ROE (5-factor) = Tax Burden × Interest Burden × EBIT Margin
                 × Asset Turnover × Financial Leverage
Tax Burden = PAT/EBT | Interest Burden = EBT/EBIT

LIQUIDITY RATIOS
──────────────────────────────────────────────────────────
Current Ratio = Current Assets / Current Liabilities
Quick Ratio = (CA - Inventory) / CL
Cash Ratio = (Cash + Marketable Securities) / CL
DSO = Trade Receivables / (Revenue/365)
DIO = Inventory / (COGS/365)
DPO = Trade Payables / (COGS/365)
CCC = DSO + DIO - DPO (lower = better)

LEVERAGE RATIOS
──────────────────────────────────────────────────────────
D/E Ratio = Total Debt / Total Equity
Debt/Assets = Total Debt / Total Assets × 100
Net Debt/EBITDA = (Debt - Cash) / EBITDA
ICR = EBIT / Interest (must be > 3x)
DSCR = Operating CF / Total Debt Service (> 1.25x)
Financial Leverage = Total Assets / Equity

EFFICIENCY RATIOS
──────────────────────────────────────────────────────────
Asset Turnover = Revenue / Total Assets
Fixed Asset Turnover = Revenue / Net Fixed Assets
Inventory Turnover = COGS / Inventory
Receivables Turnover = Revenue / Trade Receivables
Payables Turnover = COGS / Trade Payables

MARKET RATIOS
──────────────────────────────────────────────────────────
P/E Ratio = Market Price / EPS
P/B Ratio = Market Price / Book Value per Share
EV = Market Cap + Total Debt - Cash
EV/EBITDA = Enterprise Value / EBITDA
EV/Revenue = Enterprise Value / Revenue
Dividend Yield = DPS / Market Price × 100
PEG Ratio = P/E / EPS Growth Rate (< 1.5 = fair)

CASH FLOW
──────────────────────────────────────────────────────────
FCF = CFO - CapEx (Free Cash Flow)
CFO/PAT Ratio = Operating CF / Net Profit (> 1 = quality)
FCF Yield = FCF / Market Cap × 100 (> 3% = good)
Accrual Ratio = (PAT - CFO) / Avg Total Assets (< 5%)

VALUATION
──────────────────────────────────────────────────────────
Gordon Growth: P = D₁ / (Ke - g) = DPS×(1+g)/(Ke-g)
P/E Valuation: Intrinsic Price = EPS × Industry P/E
EV/EBITDA Valuation: EV = EBITDA × Multiple
                     Equity Value = EV - Net Debt

KEY RULES
──────────────────────────────────────────────────────────
- Always compare ratios to OWN history + INDUSTRY peers
- CFO/PAT > 1 = high earnings quality
- CCC: lower is better for cash efficiency
- ICR < 1.5 = financial distress signal
- Rising D/E + falling ICR = leverage risk
- PAT growing faster than Revenue = operating leverage
- FCF positive & growing = business health signal
=============================================================
"""
    st.text_area("Formula Reference",formulas,height=700)
    st.download_button("📥 Download",data=formulas,file_name="FSA_Formulas.txt")

# =========================================================
elif menu == "Common Student Mistakes":
    st.header("⚠️ Common Student Mistakes in FSA")
    mistakes=pd.DataFrame({
        "Mistake":["Using ROE instead of ROCE for capital decisions",
                   "Current Ratio: using Total Assets not CA",
                   "DuPont: adding instead of multiplying",
                   "Gross Profit Margin using EBIT not GP",
                   "ICR: using Revenue instead of EBIT",
                   "EPS: not dividing PAT by shares (or using wrong unit)",
                   "CCC = DIO + DSO + DPO (adding DPO, not subtracting)",
                   "EV = Market Cap only (forgetting debt and cash)",
                   "Inventory Turnover: using Revenue instead of COGS",
                   "Net Margin = EBIT/Revenue (should be PAT)"],
        "Correct Approach":["ROCE = EBIT/Capital Employed. ROE = PAT/Equity. For operational efficiency, ROCE is better.",
                             "Current Ratio = Current Assets / Current Liabilities. Both must be current, not total.",
                             "DuPont ROE = NM × AT × Leverage (multiply all three). Denominator of each cancels with numerator of next.",
                             "Gross Margin = Gross Profit/Revenue. GP = Revenue - COGS. EBIT includes OPEX and D&A additionally.",
                             "ICR = EBIT / Interest Expense. EBIT is earnings BEFORE interest. Tests ability to service interest.",
                             "EPS = PAT (₹) / Number of Shares. Ensure same units — both in ₹ or both in Cr.",
                             "CCC = DIO + DSO - DPO. DPO is SUBTRACTED (supplier credit reduces your cash tied up).",
                             "EV = Market Cap + Total Debt - Cash & Equivalents. This is 'enterprise' value (debt-free, cash-free).",
                             "Inventory Turnover = COGS / Inventory. Not Revenue (COGS is what flows through inventory).",
                             "Net Margin = PAT/Revenue. EBT margin = EBT/Revenue. EBIT margin = EBIT/Revenue. Each is different."]
    })
    st.table(mistakes)

# =========================================================
elif menu == "Advanced Quiz Bank":
    st.header("📝 Advanced Quiz Bank")
    level=st.selectbox("Difficulty",["Beginner","Intermediate","Advanced"])
    if level=="Beginner":
        st.markdown("""
**Problem:** Revenue=₹1000Cr, COGS=₹600Cr, OPEX=₹150Cr, Dep=₹50Cr, Interest=₹40Cr, Tax=25%
(a) Gross Profit  (b) EBITDA  (c) EBIT  (d) PAT
""")
        a1=1000-600; a2=a1-150; a3=a2-50; a4=max((a3-40)*0.75,0)
        c1,c2,c3,c4=st.columns(4)
        c1.number_input("(a) GP",value=0.0,step=1.0,key="beg_a")
        c2.number_input("(b) EBITDA",value=0.0,step=1.0,key="beg_b")
        c3.number_input("(c) EBIT",value=0.0,step=1.0,key="beg_c")
        c4.number_input("(d) PAT",value=0.0,step=0.1,key="beg_d")
        if st.button("Evaluate",key="beg_btn"):
            if all([abs(st.session_state.get(f"beg_{k}",0)-v)<1 for k,v in zip(["a","b","c","d"],[a1,a2,a3,a4])]):
                st.success(f"✅ GP={a1}, EBITDA={a2}, EBIT={a3}, PAT={a4}"); st.balloons()
            else: st.error(f"GP={a1} | EBITDA={a2} | EBIT={a3} | PAT={a4}")
    elif level=="Intermediate":
        st.markdown("""
**Problem:** PAT=₹144Cr, Revenue=₹1200Cr, Assets=₹1250Cr, Equity=₹570Cr
(a) Net Margin  (b) Asset Turnover  (c) Leverage  (d) ROE by DuPont
""")
        nm=144/1200*100; at=1200/1250; lev=1250/570; roe=nm*at*lev/100*100
        c1,c2,c3,c4=st.columns(4)
        c1.number_input("(a) Net Margin %",value=0.0,step=0.01,key="int_nm")
        c2.number_input("(b) Asset Turnover x",value=0.0,step=0.001,key="int_at")
        c3.number_input("(c) Leverage x",value=0.0,step=0.001,key="int_lev")
        c4.number_input("(d) ROE %",value=0.0,step=0.01,key="int_roe")
        if st.button("Evaluate",key="int_btn"):
            vals={"int_nm":nm,"int_at":at,"int_lev":lev,"int_roe":roe}
            if all([abs(st.session_state.get(k,0)-v)<max(0.01,v*0.02) for k,v in vals.items()]):
                st.success(f"✅ NM={round(nm,2)}%, AT={round(at,4)}x, Lev={round(lev,4)}x, ROE={round(roe,2)}%"); st.balloons()
            else: st.error(f"NM={round(nm,2)}% | AT={round(at,4)}x | Lev={round(lev,4)}x | ROE={round(roe,2)}%")
    else:
        st.markdown("""
**Advanced:** Inv=₹150Cr,COGS=₹720Cr,Debtors=₹200Cr,Rev=₹1200Cr,Creditors=₹120Cr,Cash=₹80Cr,ST_Debt=₹80Cr,LT_Debt=₹400Cr,Equity=₹570Cr,EBIT=₹240Cr,Interest=₹48Cr
(a) CCC  (b) D/E Ratio  (c) ICR  (d) Net Debt
""")
        dio_a=150/(720/365); dso_a=200/(1200/365); dpo_a=120/(720/365)
        ccc_a=dio_a+dso_a-dpo_a; de_a=(80+400)/570; icr_a=240/48; nd_a=480-80
        c1,c2,c3,c4=st.columns(4)
        c1.number_input("(a) CCC (days)",value=0.0,step=0.1,key="adv_ccc")
        c2.number_input("(b) D/E x",value=0.0,step=0.01,key="adv_de")
        c3.number_input("(c) ICR x",value=0.0,step=0.01,key="adv_icr")
        c4.number_input("(d) Net Debt (₹Cr)",value=0.0,step=1.0,key="adv_nd")
        if st.button("Evaluate",key="adv_btn"):
            vals={"adv_ccc":ccc_a,"adv_de":de_a,"adv_icr":icr_a,"adv_nd":nd_a}
            if all([abs(st.session_state.get(k,0)-v)<max(0.2,v*0.02) for k,v in vals.items()]):
                st.success(f"✅ CCC={round(ccc_a,1)}d | D/E={round(de_a,4)}x | ICR={round(icr_a,4)}x | ND=₹{nd_a}Cr"); st.balloons()
            else: st.error(f"CCC={round(ccc_a,1)}d | D/E={round(de_a,4)}x | ICR={round(icr_a,4)}x | ND=₹{nd_a}Cr")

# =========================================================
elif menu == "Progress Tracker":
    st.header("📈 Progress Tracker")
    if "fsa_completed" not in st.session_state: st.session_state.fsa_completed=[]
    if "fsa_scores" not in st.session_state: st.session_state.fsa_scores=[]
    all_modules=["Income Statement","Balance Sheet","Cash Flow Statement","Common Size Analysis",
                 "Horizontal Analysis","Liquidity Ratios","Profitability Ratios",
                 "Leverage Ratios","Efficiency Ratios","Market Ratios","DuPont Analysis",
                 "Earnings Quality","Working Capital","Trend Analysis","Inter-Firm Comparison",
                 "Red Flags","Credit Analysis","Equity Valuation","Integrated Framework"]
    selected=st.multiselect("Mark completed:",all_modules,default=st.session_state.fsa_completed)
    st.session_state.fsa_completed=selected
    col1,col2=st.columns(2)
    with col1: topic=st.selectbox("Topic",["Ratios","DuPont","Valuation","Credit Analysis","Red Flags"])
    with col2: score=st.number_input("Score (%)",0,100,75,key="fsa_score_inp")
    if st.button("Log Score"):
        st.session_state.fsa_scores.append({"topic":topic,"score":score})
        st.success("Logged!")
    n_done=len(selected); n_total=len(all_modules)
    st.metric("Modules Completed",f"{n_done}/{n_total}")
    st.progress(n_done/n_total)
    if st.session_state.fsa_scores:
        avg=sum(s["score"] for s in st.session_state.fsa_scores)/len(st.session_state.fsa_scores)
        st.metric("Average Score",f"{round(avg,1)}%")
    if n_done==n_total: st.success("🏆 All modules complete!"); st.balloons()

# =========================================================
elif menu == "Case-Based Learning — Infosys":
    st.header("📚 Case Study: Infosys Ltd. — FSA for an Equity Analyst")
    st.markdown("""
## Company Overview
Infosys is India's second-largest IT services company, with global operations.
We analyse FY2024 (approximate) data from an equity analyst's perspective.
""")
    st.subheader("Simplified P&L (FY2024 Approximate, ₹ Crore)")
    infy_is = pd.DataFrame({
        "Item":["Revenue","COGS","Gross Profit","OPEX","EBITDA","D&A","EBIT","Interest","EBT","Tax","PAT"],
        "FY2024":["₹1,53,670Cr","₹92,202Cr","₹61,468Cr","₹18,440Cr","₹43,028Cr","₹5,380Cr","₹37,648Cr","₹424Cr","₹37,224Cr","₹9,306Cr","₹26,248Cr"],
        "FY2023":["₹1,46,767Cr","₹88,059Cr","₹58,708Cr","₹17,612Cr","₹41,096Cr","₹4,690Cr","₹36,406Cr","₹350Cr","₹36,056Cr","₹9,014Cr","₹25,248Cr"],
        "% Rev FY24":["100%","60%","40%","12%","28%","3.5%","24.5%","0.3%","24.2%","6.1%","17.1%"]
    })
    st.dataframe(infy_is, use_container_width=True)

    col1,col2,col3,col4 = st.columns(4)
    col1.metric("Revenue Growth","4.7%")
    col2.metric("EBITDA Margin","28%")
    col3.metric("PAT Margin","17.1%")
    col4.metric("ICR",f"{round(37648/424,1)}x")

    st.subheader("Key Ratios")
    infy_ratios = pd.DataFrame({
        "Ratio":["Gross Margin","EBITDA Margin","Net Margin","ROE","ICR","D/E","P/E","EV/EBITDA"],
        "Infosys FY24":["40%","28%","17.1%","~30%","88.8x","Near Zero","~24x","~16x"],
        "IT Industry Avg":["35-40%","22-26%","15-18%","20-25%",">10x","<0.5x","22-28x","14-18x"],
        "Signal":["✅ In line","✅ Above avg","✅ Above avg","✅ Excellent","✅ Very strong","✅ Debt-free","✅ Fairly valued","✅ In range"]
    })
    st.dataframe(infy_ratios, use_container_width=True)

    st.subheader("Key Observations for an Analyst")
    observations = [
        "**Near debt-free balance sheet** — Interest of ₹424Cr on ₹1.5L Cr revenue is negligible. ICR = 88x!",
        "**High CFO/PAT ratio (~1.1x)** — Infosys is a cash-generating machine. PAT is high quality.",
        "**Rising attrition in FY22-23** led to higher COGS — now normalising.",
        "**Large cash balance** (₹30,000+Cr) — Capital allocation is a key question: buybacks, dividends, or acquisitions?",
        "**Revenue growth slowing** (4.7% FY24 vs 15%+ in FY22) — discretionary IT spending cuts by clients.",
        "**Margins defended** despite slowdown — cost efficiency measures effective.",
    ]
    for obs in observations:
        st.info(f"📌 {obs}")

    st.subheader("Discussion Questions")
    q_infy = st.radio("Based on FSA, what is the main risk for Infosys?",
        ["High leverage — too much debt",
         "Revenue growth deceleration in a cyclical slowdown",
         "Negative cash flow — burning cash",
         "Very low margins compared to peers"])
    if q_infy == "Revenue growth deceleration in a cyclical slowdown":
        st.success("✅ Correct! Infosys is financially very strong. The key risk is topline growth in a discretionary IT spend slowdown.")

# =========================================================
elif menu == "Case-Based Learning — Zomato":
    st.header("📚 Case Study: Zomato / Eternal Ltd. — FSA for a Growth Investor")
    st.markdown("""
## Zomato — Analysing a High-Growth, Recent Profitable Tech Company

Zomato (now Eternal Ltd.) is India's leading food delivery & quick commerce company.
It became profitable in FY2024 after years of losses. A challenging FSA case!
""")

    st.subheader("Simplified Financials (₹ Crore)")
    zomato_data = pd.DataFrame({
        "Item":["Revenue","COGS (fulfillment)","Gross Profit","Marketing/OPEX","EBITDA","D&A","EBIT","PAT","FCF"],
        "FY2022":["₹4,192Cr","₹3,350Cr","₹842Cr","₹5,800Cr","₹(4,958)Cr","₹340Cr","₹(5,298)Cr","₹(1,222)Cr","Negative"],
        "FY2023":["₹7,079Cr","₹5,663Cr","₹1,416Cr","₹4,200Cr","₹(2,784)Cr","₹394Cr","₹(3,178)Cr","₹(971)Cr","Negative"],
        "FY2024":["₹14,298Cr","₹10,007Cr","₹4,291Cr","₹3,500Cr","₹791Cr","₹450Cr","₹341Cr","₹351Cr","Turning positive"],
    })
    st.dataframe(zomato_data, use_container_width=True)

    st.subheader("The Zomato FSA Challenge")
    st.warning("""
**Traditional FSA fails for high-growth tech companies:**
- P/E ratio: useless when EPS is negative or just turning positive
- Standard ROE/ROA: not meaningful when equity base is inflated by fundraising
- Debt ratios: company is net cash positive (no debt issue)

**What works instead:**
- **Revenue growth trajectory** — from ₹4,192Cr to ₹14,298Cr in 3 years (CAGR ~50%)
- **Gross margin expansion** — from 20% to 30% (path to profitability visible)
- **EBITDA improvement** — from −₹4,958Cr to +₹791Cr (inflection point!)
- **Unit economics** — GOV (Gross Order Value), take rate, contribution per order
- **EV/Revenue** or **EV/GOV** — used when EBITDA is small
""")

    st.subheader("Key Non-Financial Metrics (Zomato)")
    kpi_data = pd.DataFrame({
        "KPI":["Monthly Transacting Users","Average Order Value","Take Rate","GOV","Market Share (Food Delivery)","Adjusted EBITDA Margin"],
        "FY2022":["~6M","₹368","~15%","₹14,000Cr","~45%","Negative"],
        "FY2024":["~18M","₹430","~17%","₹90,000Cr","~55%","~5.5%"],
        "Direction":["📈","📈","📈","📈","📈","📈"]
    })
    st.table(kpi_data)

    st.subheader("Analyst Decision: Should you invest?")
    zomato_decision = st.radio("Your recommendation on Zomato:",
        ["BUY — profitability inflection achieved; long runway ahead",
         "HOLD — watch for 2 more quarters to confirm profitability sustainability",
         "SELL — traditional ratios show it's too expensive",
         "AVOID — food delivery business model is structurally unprofitable"])

    if zomato_decision == "BUY — profitability inflection achieved; long runway ahead":
        st.success("""✅ Strong view! Key thesis:
- Revenue CAGR ~50% for 3 years
- EBITDA inflection point confirmed
- Quick commerce (Blinkit) is high-growth adjacency
- Near monopoly in urban India food delivery
- Valuation on EV/GOV or EV/Revenue justified for hypergrowth""")
    elif zomato_decision == "HOLD — watch for 2 more quarters":
        st.info("✅ Prudent view! Wait for PAT sustainability evidence before full commitment.")
    elif zomato_decision == "SELL — traditional ratios show it's too expensive":
        st.warning("⚠️ Traditional FSA is insufficient for high-growth tech companies. EV/Revenue and unit economics are better tools here.")
    else:
        st.error("❌ Too pessimistic. The unit economics have improved dramatically. Quick commerce adds another growth vector.")

    st.subheader("The Key Lesson")
    st.success("""
**For Future-Ready Managers:** FSA must adapt to the type of company:
- **Mature stable company** → All ratios apply fully
- **Cyclical company** → Focus on through-cycle average margins
- **High-growth startup** → Revenue growth, unit economics, path to profitability
- **Bank/NBFC** → NIM, NPA, CAR, not D/E ratios
- **Real Estate** → NAV, launch pipeline, collections

**One framework doesn't fit all. Context is everything in FSA.**
""")
