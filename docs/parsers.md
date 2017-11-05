
Data sources are static files (Word, PDF, html) and some open APIs. 
Parser is the python code performing requests and emitting datapoints as dictionaries 
like:

```{'name': USDRUR_CB, 'date': '2017-09-28', 'freq': 'd', 'value': 58.0102} ```


[parser-rosstat-kep](https://github.com/mini-kep/parser-rosstat-kep) supplies most time monthly series. It is supplemented by daily ruble exchange rate from Bank of Russia and oil prices from EIA and some others.

<hr>
<table>   
<tr>
    <td><b>Repository:</b></td>
    <td><a href="https://github.com/mini-kep/parsers">https://github.com/mini-kep/parsers</a>
	</td>
</tr>
</table>
