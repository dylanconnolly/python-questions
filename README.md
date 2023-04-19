## Anagram

Run the program with `python3 anagramy.py <word1> <word2>` from the command line. Additional arguments provided beyond the first two will be ignored.

## MAC Addresses

The approach was to consume the 10,000+ MAC addresses and build a queue. I would then batch the queue into a set size (100 for now, but can be adjusted based on API endpoint rate limiting or other factors). I used Python's `ThreadPoolExecutor` to make concurrent requests to the endpoint to speed the process up a bit. Each batch would write its results to the `health_check_results` file upon completion so that if a failure occured, the process could be run again from the failed batch. Since the request and data stream is mocked, there is no error handling at the moment which would be the first thing to address if the script was making actual http requests to an endpoint. 