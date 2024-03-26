import streamlit as st
st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_option('deprecation.showfileUploaderEncoding', False)
st.markdown("<h1 style='color: #0098A2;'>Prioritization Tool</h1>", unsafe_allow_html=True)

safety = st.selectbox("What influence does the task have on **Safety** ?",
                      ("NONE",
                        "5 – Completely eliminates hazard",
                       "4 – Substitutes hazard for safe alternative",
                       "3 – Isolates people from the hazard",
                       "2 – Positively changes the way people interact with the hazard",
                       "1 – No hazard risk reduction"))

quality = st.selectbox("What influence does the task have on **Quality** ?",
                      ("NONE",
                          "5 – Defect fully removed.",
                       "4 – Big improvement (75% of NCR don't exist).",
                       "3 – Quality improvement, half of defect removed",
                       "2 – Positively changes the way people interact with the hazard.",
                       "1 – No hazard risk reduction."))

capacity = st.selectbox("What influence does the task have on **Capacity** ?",
                        ("NONE",
                            "5 – 100% - Without this equipment we cannot produce",
                         "4 – Equipment will increase capacity in 75%",
                         "3 – Equipment will increase capacity in 50%",
                         "2 – Equipment will increase capacity in 25%",
                         "1 – No quality increase"))


cycle_time = st.selectbox("What influence does the task have on **Cycle time**?",
                          ("NONE",
                            "5 – Decrease cycle time more than 100%",
                           "4 – Decrease cycle time more than 75%",
                           "3 – Decrease cycle time more than 50%",
                           "2 – Decrease cycle time more than 25%",
                           "1 – No cycle time decrease"))




cost_radio=st.radio("**New project** or **Tooling Maintenance** ?", ("Project Cost","Tooling Maintenance Cost"))

if cost_radio=="Project Cost":

    project_cost = st.selectbox("What influence does the task have on Project Cost ?",
                                ("NONE",
                                    "5 – This equipment will result in a cost saving of more than 100k€ in 1 year",
                                 "4 – This equipment will result in a cost saving between 50k-100k€ in 1 year",
                                 "3 – This equipment will result in a cost saving between 25k-50k€ in 1 year",
                                 "2 – This equipment will result in a cost saving between 1k-25k€ in 1 year",
                                 "1 – This equipment doesn’t bring any cost saving"))
    projectnum = 0 if project_cost == "NONE" else int(project_cost.split("–")[0].strip())

else:

    tooling_maintenance_cost = st.selectbox("What influence does the task have on Tooling Maintenance Cost ?",
                                            ("NONE",
                                            "5 – This equipment will result in a cost saving of more than 50k€ in 1 year",
                                            "4 – This equipment will result in a cost saving between 25k-50k€ in 1 year",
                                            "3 – This equipment will result in a cost saving between 12,5k-25k€ in 1 year",
                                            "2 – This equipment will result in a cost saving between 1k-12,5k€ in 1 year",
                                            "1 – This equipment doesn’t bring any cost saving"))
    tooling_maintenance_cost_num = 0 if tooling_maintenance_cost == "NONE" else int(tooling_maintenance_cost.split("–")[0].strip())


manager_factor=st.radio("Select manager factor:",("5","4","3","2","1"))

sa_num = 0 if safety == "NONE" else int(safety.split("–")[0].strip())
q_num = 0 if quality == "NONE" else int(quality.split("–")[0].strip())
ca_num = 0 if capacity == "NONE" else int(capacity.split("–")[0].strip())
cy_num = 0 if cycle_time == "NONE" else int(cycle_time.split("–")[0].strip())


mf_num=int(manager_factor)

#results
total_sum = 0.4*(0.60*sa_num+0.15*(q_num+ca_num+cy_num))+0.6*mf_num

if cost_radio == "Project Cost":
    total_sum += 0.4*0.15*projectnum
else:
    total_sum += 0.4*0.15*tooling_maintenance_cost_num


st.write("Final Classification:", round(total_sum))

if total_sum >=4:
    prioritylvl="**Critical**"
elif total_sum>= 3:
    prioritylvl="**Major**"
elif total_sum>=2:
    prioritylvl="**Minor**"
else :
    prioritylvl="**Trivial**"


st.write("Priority level:", prioritylvl)
