import streamlit as st

pin1 = [1111, 1222, 1333]
an = [555, 666, 777]
pn = [987, 965, 985]
bb = [100, 200, 300]
cn = ["raj", "Sam", "ram"]

st.title("💳 DEMO ATM")

# ---------------- LOGIN ----------------
user = st.number_input("Enter your Account number", step=1)
pin = st.number_input("Enter your 4 digit pin", step=1)

if st.button("Login"):

    b = 0
    a = 0

    for i in an:
        if i == user:
            b = 1

    for j in range(len(an)):
        if an[j] == user:
            a = j

    if b == 1:
        if pin == pin1[a]:

            st.success("Login Successful")
            st.write("-+-+-+-+-+-+-+-+-+-+-+-+-")

            # -------- MENU --------
            st.write("Please choose option")

            opt = st.selectbox(
                "Select option",
                ["Withdraw Cash", "Account statement", "Deposit funds", "Change pin", "Exit"]
            )

            # -------- WITHDRAW --------
            if opt == "Withdraw Cash":
                user1 = st.number_input("Enter amount", step=1)
                pin_user = st.number_input("Enter pin", step=1, key="w")

                if st.button("Withdraw"):
                    if pin_user == pin1[a]:
                        if bb[a] >= user1:
                            bb[a] -= user1
                            st.write("Transaction Successful!")
                            st.write("Remaining balance is:", bb[a])
                        else:
                            st.write("Insufficient funds!")
                    else:
                        st.write("Incorrect Pin!")

            # -------- ACCOUNT STATEMENT --------
            elif opt == "Account statement":
                pin_user2 = st.number_input("Enter pin", step=1, key="s")

                if st.button("Show Statement"):
                    if pin_user2 == pin1[a]:
                        st.write("----Account Statement----")
                        st.write("customer name :", cn[a])
                        st.write("phone no      :", pn[a])
                        st.write("Account number:", an[a])
                        st.write("Current balance:", bb[a])
                    else:
                        st.write("wrong pin!")

            # -------- DEPOSIT --------
            elif opt == "Deposit funds":
                st.write("min deposit : 100 | max deposit : 1000")

                user2 = st.number_input("Enter amount", step=1, key="d")
                pin_user3 = st.number_input("Enter pin", step=1, key="dp")

                if st.button("Deposit"):
                    if pin_user3 == pin1[a]:
                        if 100 <= user2 <= 1000:
                            bb[a] += user2
                            st.write("Money deposited!")
                            st.write("Current balance:", bb[a])
                        else:
                            st.write("Invalid Amount")
                    else:
                        st.write("wrong pin!")

            # -------- CHANGE PIN --------
            elif opt == "Change pin":
                new_pin = st.number_input("Enter new pin", step=1, key="np")
                confirm_pin = st.number_input("Confirm new pin", step=1, key="cp")

                if st.button("Change PIN"):
                    if new_pin == confirm_pin:
                        pin1[a] = new_pin
                        st.write("Pin has been changed")
                    else:
                        st.write("Invalid Pin!")

            # -------- EXIT --------
            elif opt == "Exit":
                st.write("Thank you, visit again")

        else:
            st.error("Wrong pin")

    else:
        st.error("Wrong Account number")
