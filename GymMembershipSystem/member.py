class Member:

    def __init__(self, member_id, name, plan, session):
        self.member_id = member_id
        self.name = name
        self.plan = plan
        self.session = session
        self.status = True

    def member_info(self):
        if self.status:
            status = "Active"
        else:
            status = "Inactive"
        print(f"[{self.member_id}] {self.name} - Plan: {self.plan} - Session Left: {self.session} - Status: {status}")

    def check_in_session(self):
        if self.session > 0:
            self.session -= 1
            print(f"{self.name} checked into class! Session remaining: {self.session}")
            return True
        else:
            self.status = False
            print(f"{self.name} has {self.session} session left! Please renew membership.")
            return False

    def renew_membership(self, member_id, membership_session):
        if not self.status:
            self.status = True
            self.session = membership_session
            print(f"Added {membership_session} session to {self.name}. Total session: {self.session}")
        else:
            print(f"{member_id} still has {self.session} session left.")

# member = Member("M101", "Ace Malasaga", "Premium", 0)
# member.member_info()
# member.check_in_session()
# member.renew_membership("M101", 5)