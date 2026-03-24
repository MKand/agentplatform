import asyncio
import logging
import os
import random

from fastmcp import FastMCP

logger = logging.getLogger(__name__)
logging.basicConfig(format="[%(levelname)s]: %(message)s", level=logging.INFO)

mcp = FastMCP("MCP Server on Cloud Run")


@mcp.tool()
def get_fun_fact() -> str:
    """Returns a fun trivia fact to share with the user."""
    facts = [
        "A jiffy is an actual unit of time: 1/100th of a second.",
        "Octopuses have three hearts.",
        "Bananas are curved because they grow towards the sun.",
        "The Eiffel Tower can be 15 cm taller during the summer.",
        "A group of owls is called a parliament.",
        "Honey never spoils.",
        "The shortest war in history lasted only 38 minutes.",
        "The average person walks the equivalent of three times around the world in their lifetime.",
        "The world's oldest known living organism is a tree in Sweden that is over 9,500 years old.",
        "The average cloud weighs over a million pounds.",
    ]
    return random.choice(facts)


if __name__ == "__main__":
    logger.info(f"MCP server started on port {os.getenv('PORT', 8080)}")
    asyncio.run(
        mcp.run_http_async(
            transport="streamable-http",
            path="/",
            host="0.0.0.0",
            port=int(os.getenv("PORT", 8080)),
            stateless_http=True
        )
    )
