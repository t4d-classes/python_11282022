import asyncio


async def run(message: str) -> str:
    proc = await asyncio.create_subprocess_exec(
        "python",
        "echo.py",
        message,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)

    stdout, stderr = await proc.communicate()

    print(
        f'[{" ".join(["python", "echo.py", message])!r} exited with {proc.returncode}]')
    if stdout:
        return stdout.decode().strip()
    if stderr:
        print(f'[stderr]\n{stderr.decode()}')
        return ""


async def main() -> None:
    results = await asyncio.gather(
        run("a"),
        run("b"),
        run("c"))

    print(results)

asyncio.run(main())
