# -*- coding: utf-8 -*-
import httpx


async def make_api_request(api_endpoint, params):
    async with httpx.AsyncClient() as client:
        # Make the GET request to the API
        response = await client.get(api_endpoint, params=params)

        # Check the status code of the response
        if response.status_code != 200:
            print("Error: Failed to retrieve data from API")
            return None
        else:
            # Retrieve the data in JSON format
            data = response.json()
            print(data)

            return data