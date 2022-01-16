import requests

_BASE_URL_ = 'http://localhost:3001/api/'

_UNAUTHORIZED_ = 401
_NOT_FOUND_ = 404
_INVALID_KEY_ = 'Invalid API Key'
_SERVER_ERROR_ = 'Something is wrong. Please contact the creator'

class StockSymbols():
  def __init__(self, api_key: str):
      self._base_url = _BASE_URL_
      self.api_key = api_key

  def get_symbol_list(self, market=None, index=None, symbols_only=False):
    headers = {'x-api-key': self.api_key}
    try:
      if index != None:
        params = {'market': market, 'index': index}
        r = requests.get(self._base_url + 'indexes', params=params, headers=headers)
      else:
        params = {'market': market}
        r = requests.get(self._base_url + 'symbols', params=params, headers=headers)
      if r.status_code == _UNAUTHORIZED_:
        raise ValueError(_INVALID_KEY_)
      if r.status_code == _NOT_FOUND_:
        raise ValueError(r.json()['error'])
      data = r.json()['data']
      if symbols_only:
        return [q['symbol'] for q in data[0]['quotes']]
      else:
        return data[0]['quotes']
    except ValueError:
      raise
    except:
      raise Exception(_SERVER_ERROR_)

  def get_market_list(self):
    headers = {'x-api-key': self.api_key}
    try:
      r = requests.get(self._base_url + 'market/all', headers=headers)
      if r.status_code == _UNAUTHORIZED_:
        raise ValueError(_INVALID_KEY_)
      data = r.json()['data']
      return data
    except ValueError:
      raise
    except:
      raise Exception(_SERVER_ERROR_)

  def get_index_list(self):
      headers = {'x-api-key': self.api_key}
      try:
        r = requests.get(self._base_url + 'indexes/all', headers=headers)
        if r.status_code == _UNAUTHORIZED_:
          raise ValueError(_INVALID_KEY_)
        data = r.json()['data']
        return data
      except ValueError:
        raise
      except:
        raise Exception(_SERVER_ERROR_)