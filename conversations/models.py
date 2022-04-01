from django.db import models
from core import models as core_models


class Conversation(core_models.TimeStamped):

    """Conversation Model Definition"""

    participants = models.ManyToManyField(
        "users.User", related_name="conversation", blank=True
    )

    def __str__(self):
        participants = []
        for user in self.participants.all():
            participants.append(user.username)
            print(user)
        return str(", ".join(participants))

    def count_messages(self):
        return self.message.count()

    count_messages.short_description = "Number of messages"

    def count_participants(self):
        return self.participants.count()

    count_participants.short_description = "Number of participant"


class Message(core_models.TimeStamped):

    """Message Model Definition"""

    message = models.TextField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    conversation = models.ForeignKey(
        "conversations.Conversation", related_name="message", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user} says: {self.message}"
