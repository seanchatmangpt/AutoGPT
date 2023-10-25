# code_mod_debug_simple_typo_no_guidance_benchmark.py

import anyio


async def main():
    print("main")
    # await


if __name__ == "__main__":
    anyio.run(main)
