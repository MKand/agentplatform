# MIT License
#
# Copyright (c) 2025 Murat Eken
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import asyncio
import logging
import os
import random

from datetime import datetime, timedelta, timezone

from fastmcp import FastMCP 
from google.cloud import compute_v1


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
    logger.info(f"🚀 MCP server started on port {os.getenv('PORT', 8080)}")
    # Could also use 'sse' transport, host="0.0.0.0" required for Cloud Run.
    asyncio.run(
        mcp.run_http_async(
            transport="streamable-http",
            path="/",
            host="0.0.0.0",
            port=os.getenv("PORT", 8080),
            stateless_http=True
        )
    )