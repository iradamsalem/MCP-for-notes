# server.py
from mcp.server.fastmcp import FastMCP
import os

# Create an MCP server
mcp = FastMCP("AI STICKY NOTES")
notesFile = os.path.join(os.path.dirname(__file__),"notes.txt")

def fileValidation():
    if not os.path.exists(notesFile):
        with open(notesFile, "w") as file:
            file.write("")

@mcp.tool()
def newNote(message: str) -> str:
    """
    Add a new message to the notes file.

    :param message: A message to add as a note.
    :return: A confirmation that the note was saved.
    """
    fileValidation()
    with open(notesFile, "a") as file:
        file.write(message + "\n")
    return "Note saved"
@mcp.tool()
def readnote() -> str:
    """
    read and returns all notes from the file


    :return: all notes readed from the file
    """
    fileValidation()
    with open(notesFile, "r") as file:
      content=file.read().strip()
    return content or "no notes yet"
@mcp.resource("notes://latest")
def getLatestNote()->str:
    """
    read and returns last note from the file


    :return: last note from the file
    """
    fileValidation()
    with open(notesFile, "r") as file:
        content = file.readlines()
    return content[-1] if content else "no notes yet"


@mcp.prompt()
def notesSummary()->str:
    """
      summerize all notes returns the summry in a prompt


      :return: summery of the notes
      """
    fileValidation()
    with open(notesFile, "r") as file:
        content = file.read().strip()
    if not content:
        return "there are no notes yet"
    return f"Summerize the current notes {content}"