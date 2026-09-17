from gym import Gym

is_gym_operate = True
gym = Gym()

while is_gym_operate:
    print("=== HOTEL RESERVATION SYSTEM ===")
    print("1. View All Member\n2. Add a New Member\n3. Check-In Member\n4. Renew Membership\n5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        gym.view_all_member()
    elif choice == 2:
        m_id = input("Enter Member ID: ")
        m_name = input("Enter Member Name: ")
        m_plan = input("Enter Member Plan: ")
        m_session = int(input("Enter Member Session: "))
        gym.add_member(m_id, m_name, m_plan, m_session)
    elif choice == 3:
        m_id = input("Enter Member ID: ")
        gym.check_membership(m_id)
    elif choice == 4:
        m_id = input("Enter Member ID: ")
        m_session = int(input("Enter Member Session: "))
        gym.renew_membership(m_id, m_session)
    elif choice == 5:
        print("Exiting...")
        is_gym_operate = False
    else:
        print("Invalid choice. Please try again.")

