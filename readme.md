# Content Interlink Suggester

An automated tool that analyzes the content of given URLs to suggest potential interlinks based on textual similarity. This tool is designed to aid in improving site structure and internal SEO.

## Prerequisites

Before you begin, ensure you have met the following requirements:

### 1. Python Installation

- **Python:** You need Python 3.x installed on your system. If you haven't installed it, you can download it from the official [Python website](https://www.python.org/downloads/).

### 2. PyCharm Community Edition (optional, but recommended)

- **PyCharm:** This is a popular Integrated Development Environment (IDE) for Python. While it's optional, it can make working with Python projects easier. Download and install the community edition from [JetBrains' website](https://www.jetbrains.com/pycharm/download/).

### 3. Virtual Environment Setup

Using a virtual environment for Python projects is a best practice as it helps manage dependencies specific to your project.

#### Setting Up a Virtual Environment in PyCharm:

1. Click on the right bottom corner of the screen where the interpreter is showing.
2. Select "Add New Interpreter".
3. Choose "Virtual Environment".
4. Click "OK" to create the virtual environment.

### Install Required Dependencies

To install the necessary packages for the Content Interlink Suggester, run the following command:

```bash
pip install -r requirements.txt
```

## Download or Clone the Repository

To get the Content Interlink Suggester tool, you can either download it as a ZIP file or clone it using Git. Here's how you can do either:

### 1. Download as ZIP

- Navigate to the main page of the repository on GitHub.
- Click on the `Code` button (usually green).
- Select `Download ZIP`.
- Once downloaded, extract the ZIP to your desired location on your computer.

### 2. Clone using Git

If you have Git installed on your system, you can clone the repository using the following command:

```bash
git clone https://github.com/meher09/InterlinkAssistant.git
```

## Adding Links to `urls.txt`

To utilize the Content Interlink Suggester tool, you'll need to populate the `urls.txt` file with the URLs you wish to analyze for potential interlinks.

### Steps:

1. **Navigate to the Project Directory**:
   Ensure you're in the root directory of the project where the `urls.txt` file resides.

2. **Open `urls.txt`**:
   Using any text editor of your choice, open the `urls.txt` file.

3. **Add URLs**:
   - Enter each URL on a new line.
   - Ensure there's no whitespace or additional characters surrounding the URLs.

   For example:
```text
https://example.com/page1
https://example.com/page2
https://another-site.com/article
```


4. **Save and Close**:
After adding all the desired URLs, save the file and close the text editor.

With your URLs in place, you can now proceed to run the Content Interlink Suggester tool and analyze the textual similarities between the provided links.

## Running the Script

Once you've populated the `urls.txt` file with your desired links, you're ready to execute the Content Interlink Suggester tool.

### Steps:

1. **Open the Project in PyCharm**:
   If you haven't already, open the project directory in PyCharm.

2. **Run the Script**:
   - Locate the main script file in the PyCharm project explorer.
   - Right-click on the script file.
   - Select `Run` from the context menu.

3. **Enter Interlink Count**:
   When prompted, enter the number of interlinks you want for each URL. The minimum value is 1 and the maximum is 5.

4. **Set Similarity Threshold**:
   Next, you'll be prompted to specify the similarity threshold percentage, which determines how similar the content should be to be considered for interlinking. Enter a value between 0 to 100%. A higher percentage means stricter similarity requirements.

5. **Wait for the Process**:
   The tool will now analyze the textual content of the provided URLs for potential interlinks. This might take some time depending on the number and size of the URLs you've provided.

6. **Check the Output**:
   - Once the process completes, you'll find two output files in the project directory:
     - `interlink_suggestions.csv`: This file contains suggested interlinks for each URL based on textual similarity.
     - `no_suggestions.txt`: This file lists the URLs for which the tool couldn't find any suitable suggestions.

You can now review the suggestions and incorporate them as needed to enhance your site's structure and internal SEO.

## Understanding the Threshold Score

In the context of our Content Interlink Suggester tool, and many machine learning or text analysis tasks in general, a **threshold score** acts as a benchmark that a result must surpass to be considered significant or meaningful.

### 🌟 **Why is a Threshold Score Important?**

When evaluating textual similarity, not all similarity scores might be practically relevant. Some content might share minor similarities due to common words or phrases, but these aren't necessarily contextually meaningful. By setting a threshold, we ensure:

1. **Noise Reduction**: It filters out low-quality matches or those that occur simply due to coincidental word overlaps.
2. **Quality Assurance**: By focusing only on matches that exceed the threshold, we increase the chances of the recommendations being contextually apt.
3. **Customizability**: Different projects or requirements might necessitate different similarity standards. With a flexible threshold, users can adjust the tool's sensitivity to suit their specific needs.

### 🔍 **How it Works in the Tool**

In our tool, the threshold score works hand in hand with the *cosine similarity* metric. Here's a quick primer on cosine similarity:

- It calculates the cosine of the angle between two vectors. For text analysis, these vectors symbolize the TF-IDF values of words in documents.
- A cosine similarity of `1` implies the documents are identical.
- A value of `0` means the documents have no terms in common.

If you set a threshold score at, let's say `0.5`, it means you're keen on content pairs that have a similarity score equal to or greater than `0.5`. Document pairs below this threshold won't be suggested as potential interlinks.

### 🛠 **User-defined Flexibility**

The tool's adaptability shines when users are allowed to set their own threshold:

- **Diverse Blog**: A blog touching on a wide array of topics might employ a high threshold to make sure only closely related articles are suggested for interlinking.
- **General News Site**: Conversely, a broad-based news platform might adopt a lower threshold to amplify the number of potential interlinks, leveraging the wide-ranging context of news pieces.

To sum it up, the threshold score acts as a gatekeeper. Its main role is to make sure the tool's output isn't just statistically backed, but also meaningful in a real-world context.