# import wordcloud and matplotlib libraries
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Intialize the Paragraph
text = '''I'm Kaushik Goswami, a passionate professional specializing in Web Designing, Python Programming, Graphic Designing, and Content Writing. With 2 years of personal experience, I bring fresh and innovative solutions to every project. From visually appealing websites to efficient Python programs and captivating graphics, I deliver high-quality work that exceeds expectations. Let's collaborate and create remarkable digital experiences. Explore my LinkedIn page for samples and connect to discuss your project.'''

# Create a WordCloud object
wordcloud = WordCloud().generate(text)

# Display the word cloud
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()