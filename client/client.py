from fastmcp.client import Client, PythonStdioTransport
import asyncio
import os

# ======================================================
# Path to the MCP Server
# ======================================================

SERVER_FILE = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "Mcp-Server",
        "server.py"
    )
)

# ======================================================
# Create Transport & Client
# ======================================================

transport = PythonStdioTransport(SERVER_FILE)
client = Client(transport)


# ======================================================
# Main Function
# ======================================================

async def main():

    async with client:

        print("✅ Connected to Brightpeak MCP Server!")

        # ----------------------------------------------
        # List all available tools
        # ----------------------------------------------

        tools = await client.list_tools()

        print("\n========== Available Tools ==========\n")

        for tool in tools:
            print(f"Tool Name: {tool.name}")
            print(f"Description: {tool.description}")
            print("-" * 50)

        # ----------------------------------------------
        # Call list_all_courses
        # ----------------------------------------------

        print("\n========== Calling list_all_courses ==========\n")

        result = await client.call_tool("list_all_courses")

        courses = result.data["courses"]

        for course in courses:
            print(f"Course ID   : {course['course_id']}")
            print(f"Title       : {course['title']}")
            print(f"Instructor  : {course['instructor_name']}")
            print(f"Credits     : {course['credits']}")
            print("-" * 40)

        # ----------------------------------------------
        # Call get_student_profile
        # ----------------------------------------------

        print("\n========== Calling get_student_profile ==========\n")

        result = await client.call_tool(
            "get_student_profile",
            {
                "email": "omar.k@brightpeak.edu"
            }
        )

        student = result.data["data"]

        print(f"Name  : {student['name']}")
        print(f"Email : {student['email']}")
        print(f"Role  : {student['role']}")

        print("\nCourses:")

        for course in student["enrolled_courses"]:
            print(f"Course : {course['title']}")
            print(f"Grade  : {course['grade']}")
            print(f"Status : {course['status']}")
            print("-" * 30)
        print("\n========== Calling update_student_grade ==========\n")

        result = await client.call_tool(
            "update_student_grade",
            {
                "student_id": 4,
                "course_id": 3,
                "new_grade": 97.5,
                "requester_role": "INSTRUCTOR"
            }
        )

        print(result.data)
        print("\n========== Verify Updated Student ==========\n")

        result = await client.call_tool(
            "get_student_profile",
            {
                "email": "youssef.i@brightpeak.edu"
            }
        )

        student = result.data["data"]

        for course in student["enrolled_courses"]:
            print(course)
        print("\n========== Calling generate_academic_report ==========\n")

        result = await client.call_tool("generate_academic_report")

        print(result.data)
# ======================================================
# Run Client
# ======================================================

if __name__ == "__main__":
    asyncio.run(main())