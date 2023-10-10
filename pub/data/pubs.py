import csv

with open('pubs.txt') as infile, open('pubs_html.txt', 'w') as outfile:
	reader = csv.DictReader(infile, delimiter='\t')
	for row in reader:
		pdf = ''
		if row['pdf']:
			pdf = f' <a href=pub/{row["pdf"]}>[PDF]</a>'
		outfile.write (
f'''
	<tr>
		<td>
			<p class=title>
				{row['title']}
			</p>
			<p class=author>
				{row['author']}
			</p>
			<p class=metadata>
				{row['year']} <a href=https://pubmed.ncbi.nlm.nih.gov/{row['pmid']}>[PMID {row['pmid']}]</a>{pdf}
			</p>
			<p></p>
		</td>
	</tr>
'''
)