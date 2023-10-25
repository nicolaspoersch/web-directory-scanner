# Directory Scanner 🕵️‍♂️

The Directory Scanner Tool is a Python script that scans a target domain for existing directories. The tool provides the ability to customize HTTP requests, allowing you to specify custom cookies and User-Agents.

## Prerequisites

Before getting started, make sure you meet the following requirements:

- **Python 3.x**: You need to have Python 3.x installed on your system. [Download Python](https://www.python.org/downloads)

### Python Libraries

Use the pip package manager to install the following Python libraries:

```
pip install requests colorama keyboard
```

## Installation
1. Clone the repository:
```
git clone https://github.com/nicolaspoersch/web-directory-scanner
```

2. Navigate to the project directory:
```
cd web-directory-scanner
```
3. Run the script:
```
python main.py
```

## Usage

When running the script, you will be prompted to provide initial information:

1. **Target Domain:** Enter the domain you want to check (e.g., example.com).

2. **File with Directory List:** Enter the name of the file containing the list of directories to be checked. Ensure the file has the .txt extension.

3. **Custom Cookies, optional:** You can enter a custom cookie to send in HTTP requests or allow the script to generate a random one.

4. **Custom User-Agent, optional:** You can specify a custom User-Agent or allow the script to generate a random one.

## Ethical Notice👮
**Remember that this tool should be used ethically and with authorization. Unauthorized use may be illegal.**
