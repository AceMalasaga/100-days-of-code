from GymMembershipSystem.member import Member
from member import Member
class Gym:

    def __init__(self):
        self.member = {}

    def view_all_member(self):
        if not self.member:
            print("No members currently registered in the gym system.")
        else:
            print("=== ALL MEMBERS ===")
            for member in self.member.values():
                member.member_info()

    def add_member(self, member_id, member_name, member_plan, member_session, member_status=True):
        if member_id in self.member:
            print(f"Member ID '{member_id}' already exists in the system.")
            return False
        else:
            self.member[member_id] = Member(member_id, member_name, member_plan, member_session, member_status)
            return True

    def check_membership(self, member_id):
        if member_id in self.member:
            self.member[member_id].check_in_session()
            return True
        else:
            print(f"Member ID '{member_id}' not found in system.")
            return False

    def renew_membership(self, member_id, member_session):
        if member_id in self.member:
            self.member[member_id].renew_membership(member_id, member_session)
            return True
        else:
            print(f"Member ID '{member_id}' not found in system.")
            return False
# gym = Gym()
# gym.add_member("M101", "Ace Malasaga", "Premium", 0)
# gym.view_all_member()
# gym.check_membership("M101")
# gym.renew_membership("M101", 5)
# print(gym.member)