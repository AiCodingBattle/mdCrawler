Skip to main content
**Join us at Interrupt: The Agent AI Conference by LangChain on May 13 & 14 in San Francisco!**
On this page
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)![Open on GitHub](https://img.shields.io/badge/Open%20on%20GitHub-grey?logo=github&logoColor=white)
Taken from Greg Kamradt's wonderful notebook: 5_Levels_Of_Text_Splitting
All credit to him.
This guide covers how to split chunks based on their semantic similarity. If embeddings are sufficiently far apart, chunks are split.
At a high level, this splits into sentences, then groups into groups of 3 sentences, and then merges one that are similar in the embedding space.
## Install Dependencies​
```
!pip install --quiet langchain_experimental langchain_openai
```

## Load Example Data​
```
# This is a long document we can split up.withopen("state_of_the_union.txt")as f:  state_of_the_union = f.read()
```

## Create Text Splitter​
To instantiate a SemanticChunker, we must specify an embedding model. Below we will use OpenAIEmbeddings.
```
from langchain_experimental.text_splitter import SemanticChunkerfrom langchain_openai.embeddings import OpenAIEmbeddingstext_splitter = SemanticChunker(OpenAIEmbeddings())
```

**API Reference:**SemanticChunker | OpenAIEmbeddings
## Split Text​
We split text in the usual way, e.g., by invoking `.create_documents` to create LangChain Document objects:
```
docs = text_splitter.create_documents([state_of_the_union])print(docs[0].page_content)
```

```
Madam Speaker, Madam Vice President, our First Lady and Second Gentleman. Members of Congress and the Cabinet. Justices of the Supreme Court. My fellow Americans. Last year COVID-19 kept us apart. This year we are finally together again. Tonight, we meet as Democrats Republicans and Independents. But most importantly as Americans. With a duty to one another to the American people to the Constitution. And with an unwavering resolve that freedom will always triumph over tyranny. Six days ago, Russia’s Vladimir Putin sought to shake the foundations of the free world thinking he could make it bend to his menacing ways. But he badly miscalculated. He thought he could roll into Ukraine and the world would roll over. Instead he met a wall of strength he never imagined. He met the Ukrainian people. From President Zelenskyy to every Ukrainian, their fearlessness, their courage, their determination, inspires the world. Groups of citizens blocking tanks with their bodies. Everyone from students to retirees teachers turned soldiers defending their homeland. In this struggle as President Zelenskyy said in his speech to the European Parliament “Light will win over darkness.” The Ukrainian Ambassador to the United States is here tonight. Let each of us here tonight in this Chamber send an unmistakable signal to Ukraine and to the world. Please rise if you are able and show that, Yes, we the United States of America stand with the Ukrainian people. Throughout our history we’ve learned this lesson when dictators do not pay a price for their aggression they cause more chaos. They keep moving.
```

## Breakpoints​
This chunker works by determining when to "break" apart sentences. This is done by looking for differences in embeddings between any two sentences. When that difference is past some threshold, then they are split.
There are a few ways to determine what that threshold is, which are controlled by the `breakpoint_threshold_type` kwarg.
Note: if the resulting chunk sizes are too small/big, the additional kwargs `breakpoint_threshold_amount` and `min_chunk_size` can be used for adjustments.
### Percentile​
The default way to split is based on percentile. In this method, all differences between sentences are calculated, and then any difference greater than the X percentile is split. The default value for X is 95.0 and can be adjusted by the keyword argument `breakpoint_threshold_amount` which expects a number between 0.0 and 100.0.
```
text_splitter = SemanticChunker(  OpenAIEmbeddings(), breakpoint_threshold_type="percentile")
```

```
docs = text_splitter.create_documents([state_of_the_union])print(docs[0].page_content)
```

```
Madam Speaker, Madam Vice President, our First Lady and Second Gentleman. Members of Congress and the Cabinet. Justices of the Supreme Court. My fellow Americans. Last year COVID-19 kept us apart. This year we are finally together again. Tonight, we meet as Democrats Republicans and Independents. But most importantly as Americans. With a duty to one another to the American people to the Constitution. And with an unwavering resolve that freedom will always triumph over tyranny. Six days ago, Russia’s Vladimir Putin sought to shake the foundations of the free world thinking he could make it bend to his menacing ways. But he badly miscalculated. He thought he could roll into Ukraine and the world would roll over. Instead he met a wall of strength he never imagined. He met the Ukrainian people. From President Zelenskyy to every Ukrainian, their fearlessness, their courage, their determination, inspires the world. Groups of citizens blocking tanks with their bodies. Everyone from students to retirees teachers turned soldiers defending their homeland. In this struggle as President Zelenskyy said in his speech to the European Parliament “Light will win over darkness.” The Ukrainian Ambassador to the United States is here tonight. Let each of us here tonight in this Chamber send an unmistakable signal to Ukraine and to the world. Please rise if you are able and show that, Yes, we the United States of America stand with the Ukrainian people. Throughout our history we’ve learned this lesson when dictators do not pay a price for their aggression they cause more chaos. They keep moving.
```

```
print(len(docs))
```

```
26
```

### Standard Deviation​
In this method, any difference greater than X standard deviations is split. The default value for X is 3.0 and can be adjusted by the keyword argument `breakpoint_threshold_amount`.
```
text_splitter = SemanticChunker(  OpenAIEmbeddings(), breakpoint_threshold_type="standard_deviation")
```

```
docs = text_splitter.create_documents([state_of_the_union])print(docs[0].page_content)
```

```
Madam Speaker, Madam Vice President, our First Lady and Second Gentleman. Members of Congress and the Cabinet. Justices of the Supreme Court. My fellow Americans. Last year COVID-19 kept us apart. This year we are finally together again. Tonight, we meet as Democrats Republicans and Independents. But most importantly as Americans. With a duty to one another to the American people to the Constitution. And with an unwavering resolve that freedom will always triumph over tyranny. Six days ago, Russia’s Vladimir Putin sought to shake the foundations of the free world thinking he could make it bend to his menacing ways. But he badly miscalculated. He thought he could roll into Ukraine and the world would roll over. Instead he met a wall of strength he never imagined. He met the Ukrainian people. From President Zelenskyy to every Ukrainian, their fearlessness, their courage, their determination, inspires the world. Groups of citizens blocking tanks with their bodies. Everyone from students to retirees teachers turned soldiers defending their homeland. In this struggle as President Zelenskyy said in his speech to the European Parliament “Light will win over darkness.” The Ukrainian Ambassador to the United States is here tonight. Let each of us here tonight in this Chamber send an unmistakable signal to Ukraine and to the world. Please rise if you are able and show that, Yes, we the United States of America stand with the Ukrainian people. Throughout our history we’ve learned this lesson when dictators do not pay a price for their aggression they cause more chaos. They keep moving. And the costs and the threats to America and the world keep rising. That’s why the NATO Alliance was created to secure peace and stability in Europe after World War 2. The United States is a member along with 29 other nations. It matters. American diplomacy matters. American resolve matters. Putin’s latest attack on Ukraine was premeditated and unprovoked. He rejected repeated efforts at diplomacy. He thought the West and NATO wouldn’t respond. And he thought he could divide us at home. Putin was wrong. We were ready. Here is what we did. We prepared extensively and carefully. We spent months building a coalition of other freedom-loving nations from Europe and the Americas to Asia and Africa to confront Putin. I spent countless hours unifying our European allies. We shared with the world in advance what we knew Putin was planning and precisely how he would try to falsely justify his aggression. We countered Russia’s lies with truth. And now that he has acted the free world is holding him accountable. Along with twenty-seven members of the European Union including France, Germany, Italy, as well as countries like the United Kingdom, Canada, Japan, Korea, Australia, New Zealand, and many others, even Switzerland. We are inflicting pain on Russia and supporting the people of Ukraine. Putin is now isolated from the world more than ever. Together with our allies –we are right now enforcing powerful economic sanctions. We are cutting off Russia’s largest banks from the international financial system. Preventing Russia’s central bank from defending the Russian Ruble making Putin’s $630 Billion “war fund” worthless. We are choking off Russia’s access to technology that will sap its economic strength and weaken its military for years to come. Tonight I say to the Russian oligarchs and corrupt leaders who have bilked billions of dollars off this violent regime no more. The U.S. Department of Justice is assembling a dedicated task force to go after the crimes of Russian oligarchs. We are joining with our European allies to find and seize your yachts your luxury apartments your private jets. We are coming for your ill-begotten gains. And tonight I am announcing that we will join our allies in closing off American air space to all Russian flights – further isolating Russia – and adding an additional squeeze –on their economy. The Ruble has lost 30% of its value. The Russian stock market has lost 40% of its value and trading remains suspended. Russia’s economy is reeling and Putin alone is to blame. Together with our allies we are providing support to the Ukrainians in their fight for freedom. Military assistance. Economic assistance. Humanitarian assistance. We are giving more than $1 Billion in direct assistance to Ukraine. And we will continue to aid the Ukrainian people as they defend their country and to help ease their suffering. Let me be clear, our forces are not engaged and will not engage in conflict with Russian forces in Ukraine. Our forces are not going to Europe to fight in Ukraine, but to defend our NATO Allies – in the event that Putin decides to keep moving west. For that purpose we’ve mobilized American ground forces, air squadrons, and ship deployments to protect NATO countries including Poland, Romania, Latvia, Lithuania, and Estonia. As I have made crystal clear the United States and our Allies will defend every inch of territory of NATO countries with the full force of our collective power. And we remain clear-eyed. The Ukrainians are fighting back with pure courage. But the next few days weeks, months, will be hard on them. Putin has unleashed violence and chaos. But while he may make gains on the battlefield – he will pay a continuing high price over the long run. And a proud Ukrainian people, who have known 30 years of independence, have repeatedly shown that they will not tolerate anyone who tries to take their country backwards. To all Americans, I will be honest with you, as I’ve always promised. A Russian dictator, invading a foreign country, has costs around the world. And I’m taking robust action to make sure the pain of our sanctions is targeted at Russia’s economy. And I will use every tool at our disposal to protect American businesses and consumers. Tonight, I can announce that the United States has worked with 30 other countries to release 60 Million barrels of oil from reserves around the world. America will lead that effort, releasing 30 Million barrels from our own Strategic Petroleum Reserve. And we stand ready to do more if necessary, unified with our allies. These steps will help blunt gas prices here at home. And I know the news about what’s happening can seem alarming.
```

```
print(len(docs))
```

```
4
```

### Interquartile​
In this method, the interquartile distance is used to split chunks. The interquartile range can be scaled by the keyword argument `breakpoint_threshold_amount`, the default value is 1.5.
```
text_splitter = SemanticChunker(  OpenAIEmbeddings(), breakpoint_threshold_type="interquartile")
```

```
docs = text_splitter.create_documents([state_of_the_union])print(docs[0].page_content)
```

```
Madam Speaker, Madam Vice President, our First Lady and Second Gentleman. Members of Congress and the Cabinet. Justices of the Supreme Court. My fellow Americans. Last year COVID-19 kept us apart. This year we are finally together again. Tonight, we meet as Democrats Republicans and Independents. But most importantly as Americans. With a duty to one another to the American people to the Constitution. And with an unwavering resolve that freedom will always triumph over tyranny. Six days ago, Russia’s Vladimir Putin sought to shake the foundations of the free world thinking he could make it bend to his menacing ways. But he badly miscalculated. He thought he could roll into Ukraine and the world would roll over. Instead he met a wall of strength he never imagined. He met the Ukrainian people. From President Zelenskyy to every Ukrainian, their fearlessness, their courage, their determination, inspires the world. Groups of citizens blocking tanks with their bodies. Everyone from students to retirees teachers turned soldiers defending their homeland. In this struggle as President Zelenskyy said in his speech to the European Parliament “Light will win over darkness.” The Ukrainian Ambassador to the United States is here tonight. Let each of us here tonight in this Chamber send an unmistakable signal to Ukraine and to the world. Please rise if you are able and show that, Yes, we the United States of America stand with the Ukrainian people. Throughout our history we’ve learned this lesson when dictators do not pay a price for their aggression they cause more chaos. They keep moving.
```

```
print(len(docs))
```

```
25
```

### Gradient​
In this method, the gradient of distance is used to split chunks along with the percentile method. This method is useful when chunks are highly correlated with each other or specific to a domain e.g. legal or medical. The idea is to apply anomaly detection on gradient array so that the distribution become wider and easy to identify boundaries in highly semantic data. Similar to the percentile method, the split can be adjusted by the keyword argument `breakpoint_threshold_amount` which expects a number between 0.0 and 100.0, the default value is 95.0.
```
text_splitter = SemanticChunker(  OpenAIEmbeddings(), breakpoint_threshold_type="gradient")
```

```
docs = text_splitter.create_documents([state_of_the_union])print(docs[0].page_content)
```

```
Madam Speaker, Madam Vice President, our First Lady and Second Gentleman.
```

```
print(len(docs))
```

```
26
```

#### Was this page helpful?
  * Install Dependencies
  * Load Example Data
  * Create Text Splitter
  * Split Text
  * Breakpoints
    * Percentile
    * Standard Deviation
    * Interquartile
    * Gradient


