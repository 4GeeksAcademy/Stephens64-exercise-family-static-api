"""
Update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = []

    # read-only: Use this method to generate random member ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # Add logic to append a new member to the list
        # Ensure 'id' exists, if not, generate it
        if 'id' not in member:
            member['id'] = self._generateId()
        
        # Ensure the last name is 'Jackson' for all members
        member['last_name'] = self.last_name

        # Append the member to the _members list
        self._members.append(member)

    def delete_member(self, id):
        # Loop through the list and remove the member with the given id
        self._members = [member for member in self._members if member['id'] != id]

    def get_member(self, id):
        # Loop through the members to find the one with the matching id
        for member in self._members:
            if member['id'] == id:
                return member
        return None

    def update_member(self, id, updated_member):
        # Update the member with the given id by looping through the list
        for index, member in enumerate(self._members):
            if member['id'] == id:
                # Ensure the last name remains 'Jackson'
                updated_member['last_name'] = self.last_name
                # Update the member information
                self._members[index] = {**member, **updated_member}
                return self._members[index]
        return None

    # This method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
