# The site supports quite a lot of languages
# all thanks to the magic of highlight.js

def is_supported(language):
    if language == "python": return "YES!"
    if language == "javascript": return "Of course"
    if language == "html": return "👍"
    if language == "css": return "cool"
    if language == "go": return "let's go"
    if language == "typescript": return "yep"
    if language == "bash": return "sure"
    if language == "c++": return "hard core, let's go"
    if language == "c#": return "game on"
    if language == "markdown": return "I'm down with that"
    if language == "ruby": return "Runs like it's on rails"
    if language == "java": return "brews fine"
    if language == "kotlin": return "all day long"
    if language == "less": return "give me more"
    if language == "php": return "ok fine, if you insist"
    if language == "R": return "good for me"
    if language == "sql": return "of course!"
    if language == "swift": return "you bet"
    
    if language in 196_supported_languages:
        return "It will almost certainly work"