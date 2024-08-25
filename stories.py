"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a code, a title, a list of prompts,
    and the text of the template.

        >>> s = Story(
        ...     "simple",
        ...     "A Simple Tale",
        ...     ["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, code, title, words, text):
        """Create story with words and template text."""

        self.code = code
        self.title = title
        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story1 = Story(
    "history",
    "A History Tale",
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

story2 = Story(
    'dream',
    'Dream State',
    ['adjective','color','thing','place','person','adjective1','insect','food','verb','verb1'],
'''Last night I dreamed I was a {adjective} butterfly with {color} splocthes that looked like {thing}. I flew to {place} with my bestfriend and {person} who was a {adjective1} {insect}. We ate some {food} when we got there and then decided to {verb} and the dream ended when I said-- lets {verb1}.''')


# Make dict of {code:story, code:story, ...}
stories = {story.code: story for story in [story1, story2]}