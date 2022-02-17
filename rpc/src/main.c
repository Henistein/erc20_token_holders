#include <iostream>
#include <stdlib.h>
#include <assert.h>
#include <curl/curl.h>
#include <nlohmann/json.hpp>

using json = nlohmann::json;
using namespace std;

static size_t write_callback(void *buffer, size_t size, 
                             size_t nmemb, string *s){
	size_t newLength = size*nmemb;
  try{
    s->append((char*)buffer, newLength); 
  }
  catch(bad_alloc &e){
    return 0; 
  }
  return newLength;
}

CURL *init_curl(char const *url){
	// get a curl handle 
	CURL *curl = curl_easy_init();

  // build headers
  struct curl_slist *headers = NULL;
  headers = curl_slist_append(headers, "Accept: application/json");
  headers = curl_slist_append(headers, "Content-Type: application/json");
  headers = curl_slist_append(headers, "charset: utf-8");

  // set the URL
  curl_easy_setopt(curl, CURLOPT_URL, url);
  // set the headers
  curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);

  return curl;
}

string get_data_fromcurl(CURL *curl, char const *data){
  string s;

  // pass our own write function, to store output into string
  curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, write_callback);
  curl_easy_setopt(curl, CURLOPT_WRITEDATA, &s);

  // specify the POST data
  curl_easy_setopt(curl, CURLOPT_POSTFIELDS, data);

  // Perform the request, res will get the return code 
  CURLcode res = curl_easy_perform(curl);
  assert(res == 0);
  
  // always clean
  curl_easy_cleanup(curl);
	curl_global_cleanup();

  return s;
}

int main(void){
  //std::string data = "{\"jsonrpc\":\"2.0\",\"method\":\"eth_getBalance\",\"params\":[\"0xDf1B72FC1bA5a77DD6c038DC2bc70746fFCA5caA\", \"latest\"],\"id\":1}";
  char const *data = "{\"jsonrpc\":\"2.0\",\"method\":\"eth_getBlockByNumber\",\"params\":[\"0xb457cf\", true],\"id\":1}";


  // init curl
	CURL *curl = init_curl("https://node.cheapeth.org/rpc");
  string out = get_data_fromcurl(curl, data);


  //json
  json j = json::parse(out);
  json result = j["result"];


  //std::cout << j.dump() << std::endl;
  std::cout << result["transactions"] << std::endl;



	return 0;
}
