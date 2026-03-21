from langchain_tavily import TavilySearch


#----------------------------------------------------------------------------------------------------
tavily_search = TavilySearch(max_results=5, topic="general", search_depth="advanced", 
                             include_raw_content=False, include_answer=False)

#-----------------------------------------------------------------------------------------------------
