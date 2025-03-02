class Ticket:
    def __init__(self, id, category, priority):
        self.id = id
        self.category = category
        self.priority = priority

class SupportAgent:
    def __init__(self, name, expertise, available=True):
        self.name = name
        self.expertise = expertise
        self.available = available

def assign_ticket_to_agent(ticket, agents):
    for agent in agents:
        if agent.available and ticket.category in agent.expertise:
            agent.available = False
            return f"Ticket {ticket.id} assigned to {agent.name}"
    return f"No suitable agent available for Ticket {ticket.id}"

if __name__ == "__main__":
    ticket1 = Ticket(101, "Technical", 1)
    ticket2 = Ticket(102, "Billing", 2)

    agents = [
        SupportAgent("Alice", ["Technical", "Sales"]),
        SupportAgent("Bob", ["Billing"], available=True),
        SupportAgent("Charlie", ["Technical"], available=False)
    ]

    print(assign_ticket_to_agent(ticket1, agents))
    print(assign_ticket_to_agent(ticket2, agents))
