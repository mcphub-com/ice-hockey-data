import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/BroadageSports/api/ice-hockey-data'

mcp = FastMCP('ice-hockey-data')

@mcp.tool()
def tournament_standings(tournamentId: Annotated[Union[int, float], Field(description='The id of the tournament. Default: 6')]) -> dict: 
    '''Team Rankings for a specific competition.'''
    url = 'https://ice-hockey-data.p.rapidapi.com/tournament/standings'
    headers = {'x-rapidapi-host': 'ice-hockey-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'tournamentId': tournamentId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def daily_match_list_scheduled(date: Annotated[str, Field(description='The date of the match. The format is {dd/MM/yyyy}. Match list data can be retrieved for only ± 7 days.')]) -> dict: 
    '''Daily match list including scheduled matches. **The data will return for only -+7 days period, so endpoint can be tested with date range of today - 7 days.**'''
    url = 'https://ice-hockey-data.p.rapidapi.com/match/list/scheduled'
    headers = {'x-rapidapi-host': 'ice-hockey-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def tournament_teams(tournamentId: Annotated[Union[int, float], Field(description='The id of the tournament. Default: 6')]) -> dict: 
    '''List of teams participating in a specific tournament.'''
    url = 'https://ice-hockey-data.p.rapidapi.com/tournament/teams'
    headers = {'x-rapidapi-host': 'ice-hockey-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'tournamentId': tournamentId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def tournament_info(tournamentId: Annotated[Union[int, float], Field(description='The id of the tournament. Default: 6')]) -> dict: 
    '''Current season, stage structure(divisions,conferences etc.), country and many more information about a tournament.'''
    url = 'https://ice-hockey-data.p.rapidapi.com/tournament/info'
    headers = {'x-rapidapi-host': 'ice-hockey-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'tournamentId': tournamentId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def tournament_fixture(tournamentId: Annotated[Union[int, float], Field(description='The id of the tournament. Default: 6')]) -> dict: 
    '''Full match list with period and final scores.'''
    url = 'https://ice-hockey-data.p.rapidapi.com/tournament/fixture'
    headers = {'x-rapidapi-host': 'ice-hockey-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'tournamentId': tournamentId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def tournament_list() -> dict: 
    '''List of tournaments in your data coverage.'''
    url = 'https://ice-hockey-data.p.rapidapi.com/tournament/list'
    headers = {'x-rapidapi-host': 'ice-hockey-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def daily_match_list_all(date: Annotated[str, Field(description='The date of the match. The format is {dd/MM/yyyy}. Match list data can be retrieved for only ± 7 days.')]) -> dict: 
    '''Daily match list including scheduled, live and finished matches. **The data will return for only -+7 days period, so endpoint can be tested with date range of today - 7 days.**'''
    url = 'https://ice-hockey-data.p.rapidapi.com/match/list'
    headers = {'x-rapidapi-host': 'ice-hockey-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def daily_match_list_live(date: Annotated[str, Field(description='The date of the match. The format is {dd/MM/yyyy}. Match list data can be retrieved for only ± 7 days.')]) -> dict: 
    '''Daily match list including live matches. **The data will return for only -+7 days period, so endpoint can be tested with date range of today - 7 days.**'''
    url = 'https://ice-hockey-data.p.rapidapi.com/match/list/live'
    headers = {'x-rapidapi-host': 'ice-hockey-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def daily_match_list_results(date: Annotated[str, Field(description='The date of the match. The format is {dd/MM/yyyy}. Match list data can be retrieved for only ± 7 days.')]) -> dict: 
    '''Daily match list including finished matches. **The data will return for only -+7 days period, so endpoint can be tested with date range of today - 7 days.**'''
    url = 'https://ice-hockey-data.p.rapidapi.com/match/list/results'
    headers = {'x-rapidapi-host': 'ice-hockey-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def recent_match_list(matchId: Annotated[Union[int, float], Field(description='The id of the match. Default: 106557')]) -> dict: 
    '''Provides the result list of the last 20 matches between the two teams in overall, with home and away filters. **The data will return for only -+7 days period, so endpoint can be tested with match that its date is in today +- 7 days. You can choose suitable match from Ice Hockey Match List or Fixture endpoints.**'''
    url = 'https://ice-hockey-data.p.rapidapi.com/h2h/match/list/recent'
    headers = {'x-rapidapi-host': 'ice-hockey-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'matchId': matchId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
