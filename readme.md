#modsqual

(This is still very much in progress, so use at your own risk! Constructive feedback and pull requests welcome.)

modsqual is a Python library to help you evaluate the quality of your MODS metadata. First and foremost, modsqual aims to make the work of parsing XML easier, so you can spend more time working with your metadata content. modsqual provides a wrapper around the popular lxml Python library, to simplify common quality control tasks, like testing for the existing of an element, counting instances of an element, and searching elements by attribute value, text match, or regular expression.   

modsqual also provides multiple representations of MODS elements to best suit the tools and skills you have at hand. modsqual can return elements in XML, Python ordered dictionaries, or just the text values of an top-level element.   

##Usage

(requires [lxml](http://lxml.de/) and [xmltodict](https://github.com/martinblech/xmltodict))  


To create a MODS object, pass a MODS XML document to the Mods class:  

```python
import modsqual

f = open('sample1.xml', 'rb')
modsdoc = read(f)
record = modsqual.Mods(modsdoc)
```

###Well-formed XML and element existence

Check that the document is wellformed:  

```python
>>> print record.wf  

True
```

Each top-level MODS element is represented as an attribute of the Mods object. Check if the name element exists in the MODS document:

```python
>>> print record.name.exists  

True  
```

###Element counts

View the counts of top-level elements present in your MODS object:

```python
>>> print record.counts  

{u'genre': 1,

 u'identifier': 6,
 u'location': 1,
 u'name': 2,
 u'originInfo': 1,
 u'physicalDescription': 1,
 u'relatedItem': 1,
 u'subject': 3,
 u'titleInfo': 1,
 u'typeOfResource': 1}
 ```

Return the count of a top-level element in the MODS document:

```python
>>> print record.subject.count  

3  
```


###Matching elements and values

The match() function allows you to return matching elements by attribute value, regular expression, or xpath. This function is a wrapper around the etree.XPath method and returns a list of xpath results. Depending on your query, this will either be a list of text values or a list of elements. You can then convert element results to Python dictionaries using the todict() function.

Given a list of attribute values of the element, returns matching instances of that element, To match by attribute, specify as attribute="attr value" in a comma-delimited list, ex. `['@authority="lcnaf"']`:

```python
>>> print record.name.match(attr=['@authority="naf"']) 

[<Element {http://www.loc.gov/mods/v3}name at 0x44c8d08>,
 <Element {http://www.loc.gov/mods/v3}name at 0x48d25c8>]
 
>>> print todict(record.name.match(attr=['@authority="naf"']))

[OrderedDict([(u'name', OrderedDict([(u'@xmlns', u'http://www.loc.gov/mods/v3'), (u'@xmlns:xsi', u'http://www.w3.org/2001/XMLSchema-instance'), (u'@type', u'personal'), (u'@usage', u'primary'), (u'@authority', u'naf'), (u'@valueURI', u'http://id.loc.gov/authorities/names/n97874402'), (u'role', OrderedDict([(u'roleTerm', [OrderedDict([(u'@authority', u'marcrelator'), (u'@type', u'code'), ('#text', u'ltg')]), OrderedDict([(u'@authority', u'marcrelator'), (u'@valueURI', u'http://id.loc.gov/vocabulary/relators/ltg'), (u'@type', u'text'), ('#text', u'Lithographer')])])])), (u'namePart', u'Delpech, Fran\xe7ois S\xe9raphin, 1778-1825')]))]), OrderedDict([(u'name', OrderedDict([(u'@xmlns', u'http://www.loc.gov/mods/v3'), (u'@xmlns:xsi', u'http://www.w3.org/2001/XMLSchema-instance'), (u'@type', u'personal'), (u'@authority', u'naf'), (u'@valueURI', u'http://id.loc.gov/authorities/names/n97861896'), (u'role', OrderedDict([(u'roleTerm', OrderedDict([(u'@authority', u'marcrelator'), (u'@type', u'code'), ('#text', u'att')]))])), (u'namePart', u'Lecomte, Hippolyte, 1781-1857')]))])]
```



Use any regular expression to match text values in the top-level element or its children:

```python
#returns all <identifier> values starting with 4 or more numbers
>>> print record.identifier.match(regex='^[0-9]{4,}')  

[1616195, 693446, 33333159165923L]
```

Use the `g` or `i` flags for refining regex:  
 `g` = global match - the submatches from all the matches in the string are returned. If this character is not present, then only the submatches from the first match in the string are returned.  
`i` = case insensitive - the regular expression is treated as case insensitive. If this character is not present, then the regular expression is case sensitive.

You can also use xpath to find elements or values within the Mods object or any top-level element. Xpaths should treat parent MODS as root and include the top-level element's tag. (ex. `./m:subject[*[@authority="lcsh"]]`) Prepend any element tags with namespace `m:`  

```python
>>> divisions = record.location.match(xpath='./m:location[m:physicalLocation[@type="division"]]')
print divisions

[<Element {http://www.loc.gov/mods/v3}location at 0x44c8b08>,
 <Element {http://www.loc.gov/mods/v3}location at 0x47a5b88>]
 
>>> todict(divisions)

[OrderedDict([(u'location', OrderedDict([(u'@xmlns', u'http://www.loc.gov/mods/v3'), (u'@xmlns:xsi', u'http://www.w3.org/2001/XMLSchema-instance'), (u'physicalLocation', [OrderedDict([(u'@authority', u'marcorg'), (u'@type', u'repository'), ('#text', u'nn')]), OrderedDict([(u'@type', u'division'), ('#text', u'Jerome Robbins Dance Division')]), OrderedDict([(u'@type', u'division_short_name'), ('#text', u'Jerome Robbins Dance Division')]), OrderedDict([(u'@type', u'code'), ('#text', u'DAN')])])]))]), OrderedDict([(u'location', OrderedDict([(u'@xmlns', u'http://www.loc.gov/mods/v3'), (u'@xmlns:xsi', u'http://www.w3.org/2001/XMLSchema-instance'), (u'shelfLocator', u'*MGZFD Del F Bal 1'), (u'physicalLocation', [OrderedDict([(u'@type', u'division'), ('#text', u'Jerome Robbins Dance Division')]), OrderedDict([(u'@type', u'division_short_name'), ('#text', u'Jerome Robbins Dance Division')]), OrderedDict([(u'@type', u'code'), ('#text', u'DAN')])])]))])]
```

###Data structures

For each top-level element, you can output data as a list of XML fragments:  

```python
>>> print record.subject.xml()  

['<subject xmlns="http://www.loc.gov/mods/v3" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" authority="lcsh">\n  <geographic authority="naf" valueURI="http://id.loc.gov/authorities/names/n78095330">United States</geographic>\n</subject>\n', '<subject xmlns="http://www.loc.gov/mods/v3" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" authority="lcsh" valueURI="http://id.loc.gov/authorities/subjects/sh85056660">\n  <geographic authority="naf" valueURI="http://id.loc.gov/authorities/names/n79023147">Great Britain</geographic>\n  <topic authority="lcsh" valueURI="http://id.loc.gov/authorities/subjects/sh99005254">Colonies</topic>\n  <geographic authority="lcsh" valueURI="http://id.loc.gov/authorities/subjects/sh85004220">America</geographic>\n</subject>\n', '<subject xmlns="http://www.loc.gov/mods/v3" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" authority="lcsh" valueURI="http://id.loc.gov/authorities/subjects/sh85092455">\n  <geographic authority="lcsh" valueURI="http://id.loc.gov/authorities/subjects/sh85092455">North America</geographic>\n</subject>\n']
```

an Ordered Dict:
```python
>>> print record.subject.dict  

[OrderedDict([(u'subject', OrderedDict([(u'@xmlns', u'http://www.loc.gov/mods/v3'), (u'@xmlns:xsi', u'http://www.w3.org/2001/XMLSchema-instance'), (u'@authority', u'lcsh'), (u'geographic', OrderedDict([(u'@authority', u'naf'), (u'@valueURI', u'http://id.loc.gov/authorities/names/n78095330'), ('#text', u'United States')]))]))]), OrderedDict([(u'subject', OrderedDict([(u'@xmlns', u'http://www.loc.gov/mods/v3'), (u'@xmlns:xsi', u'http://www.w3.org/2001/XMLSchema-instance'), (u'@authority', u'lcsh'), (u'@valueURI', u'http://id.loc.gov/authorities/subjects/sh85056660'), (u'geographic', [OrderedDict([(u'@authority', u'naf'), (u'@valueURI', u'http://id.loc.gov/authorities/names/n79023147'), ('#text', u'Great Britain')]), OrderedDict([(u'@authority', u'lcsh'), (u'@valueURI', u'http://id.loc.gov/authorities/subjects/sh85004220'), ('#text', u'America')])]), (u'topic', OrderedDict([(u'@authority', u'lcsh'), (u'@valueURI', u'http://id.loc.gov/authorities/subjects/sh99005254'), ('#text', u'Colonies')]))]))]), OrderedDict([(u'subject', OrderedDict([(u'@xmlns', u'http://www.loc.gov/mods/v3'), (u'@xmlns:xsi', u'http://www.w3.org/2001/XMLSchema-instance'), (u'@authority', u'lcsh'), (u'@valueURI', u'http://id.loc.gov/authorities/subjects/sh85092455'), (u'geographic', OrderedDict([(u'@authority', u'lcsh'), (u'@valueURI', u'http://id.loc.gov/authorities/subjects/sh85092455'), ('#text', u'North America')]))]))])]
```

or a list of text values:

```python
# complex subjects are delimited by '--' by default
>>> print record.subject.text()  

['United States', 'Great Britain -- Colonies -- America', 'North America']
```

###lxml

If you're familiar with [lxml objecify](http://lxml.de/objectify.html), you can treat any top-level element as an lxml object by calling the mods attribute:

```python
>>> print record.titleInfo.mods  

<Element {http://www.loc.gov/mods/v3}subject at 0x4146a88>
```



