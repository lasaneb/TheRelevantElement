# TheRelevantElement

## Executive Summery

Our creation deals heavily with process atomization, data categorization, and analyzation. These three components are essential to the world of FinTech. Using Natural Language Processing modules to better understand data and make actionable decisions with the information obtained to possibly capitalize on investment opportunities, increase market share, or to better serve clients is what Fintech is all about. We have also integrated the means to conduct financial transactions using digital wallets and cryptocurrencies. 

## The Challenge

Our client, a talk show radio host, is interested in a more time efficient and effective way to research daily content to discuss with his listeners. Our client has the daily task of searching the internet and sorting through thousands of articles for relevant content to discuss. We were presented with the challenge of creating a way to automate this process for the sake of time efficiency. Our client also is interested in generating social media content for further listener engagement when off air. 

## The Solution

The following packages, applications, and modules were used:
  + Streamlit
  + NewsAPI
  + Flair
  + Google Text to Speech (GTTS)
  + Solidity
  + REMIX
  + Ganache
  + MetaMask
  + Wombo.Art
  + Shutil
  + Selenium / Helium
  + Global (GLOB)

### User Interface
Steamlit was used to create the user interface. The below code was written to create the home page with various tabs.

![main infrastructure that builds app with tabs](https://user-images.githubusercontent.com/89284547/155062829-0b05cc14-f267-4d6c-a97f-e3018ea84450.jpg)

Here is what the users sees:
![Steamlit_Homepage](homepage needed)

The app allows the user to:

__Gathering, Analyzation and Sort__
_NewsApi_ allows the user search multiple news sources for realvant news articles based on desired dates, subjects or keywords.

![API_CODE](https://user-images.githubusercontent.com/89284547/155064790-edd2fb85-6bd8-46e6-b009-6d2f02dad50b.png)

_Flair_ was used the analyzie the content of the articles to determine if the article has an overall Positive or Negative setiment. 

![Flair_Code](https://user-images.githubusercontent.com/89284547/155065970-2a71c43c-8248-4987-93c5-8528b3eae257.png)

The _Flair_ module was then used to assign a grade of confidence to the setiment determination.

![Flair_Csv](https://user-images.githubusercontent.com/89284547/155066114-522342ec-cbf3-4772-bf40-b5be25a9007e.png)

__Wombo.Art__
_Wombo.Art_ was used to generate our art collection for soccial media post and engagement.

![Wombo](https://user-images.githubusercontent.com/89284547/155226817-ee06249f-69f5-4167-ac0c-1f412c5e0820.mp4)

__Revenue Generation__
_Solidity_, _REMIX_, _Ganache_, and _MetaMask_ were used to implement our revenue generating functions. The owenr of the application will be to collect donations for digital wallets.

<<<<<<< HEAD
![Donation_WalkThru](https://user-images.githubusercontent.com/89284547/155192857-ab1ec42d-ac8c-4035-8182-cc9456e1c925.mp4)
=======

## Project Challenges 

<p> Andrew H. encountered an issue when installing the Flair module. This resulted in his inability to run sentiment analysis on the dataframe that contained the articles. The solution to this was to provide him with a pre-generated datafrom where the sentiment analysis was already performed and stored in new columns. Andrew M initially encountered the issue of displaying multiple tabs within the streamlit application. The solution was to use starter code found by using an internet search for any open source code that would accomplish this function. Starter code was found and enhanced to show tabs displayed as radio buttons on the sidebar.

  
## Further Development
<p> Further development will be primarily driven by client input. Input fields will be added to allow the client to run article searches with different keywords. The app will also be deployed usingthe streamlit cloud. The bank account smart contract will be deployed to the Ethereum Mainnet. The artworks will be used to mint and sell NFTs. A web hosting service such as GoDaddy.com will be used to buy a domain. A website builder such as Wix.com in conjuction with the deployed streamlit app will be used to further enhance the front-end client interface. The client and development team will enhance the monitization by requiring a donation each time a new set of articles is requested. Alternativly, the team will consider a monthly subscription service as the primary method to monitize this service.
  
__Wombo.Art__
>>>>>>> 9cfa5e75e4304c2361be29536233535ea8c55fcb


__Backend Functionality__
Shutil
Selenium / Helium
Glob

