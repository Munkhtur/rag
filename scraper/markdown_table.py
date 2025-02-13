import markdownify

html = """
<div class="clearfix text-formatted field field--name-field-body field--type-text-long field--label-hidden field__item"><h2>Хүү шимтгэлийн ерөнхий нөхцөл</h2><hr><div class="table-responsive"><table><thead><tr><th colspan="2"><p class="text-align-center"><strong>Хүү шимтгэл</strong></p></th><th><p class="text-align-center"><strong>Төгрөг</strong></p></th></tr></thead><tbody><tr><td colspan="2">Элсэлтийн хураамж</td><td><p class="text-align-center">Хураамжгүй</p></td></tr><tr><td colspan="2">Худалдаалах үнэ</td><td><p class="text-align-center">Үнэгүй</p></td></tr><tr><td colspan="2">Карт дахин захиалах шимтгэл</td><td>5,000 төгрөг</td></tr><tr><td colspan="2">АТМ-аас бэлэн мөнгө авах лимит</td><td>3,000,000 төгрөг</td></tr><tr><td colspan="2">Худалдан авалт хийх болон бэлэн мөнгө авах лимит</td><td>3,000,000 төгрөг</td></tr><tr><td rowspan="3">АТМ-аас бэлэн мөнгө авах</td><td>ХХБ-ны&nbsp;</td><td>100₮</td></tr><tr><td>ХХБ-ны гэрээт банкны&nbsp;</td><td>300₮</td></tr><tr><td>Бусад банкны</td><td>500₮</td></tr><tr><td rowspan="3">Салбар, ТТ-өөс бэлэн мөнгө авах</td><td>ХХБ-ны</td><td>200₮</td></tr><tr><td>ХХБ-ны гэрээт банкны&nbsp;</td><td>300₮</td></tr><tr><td>Бусад банкны</td><td>500₮</td></tr></tbody></table></div></div>
"""
h = markdownify.markdownify(html, heading_style="UNDERLINED ")

print(h)


# from bs4 import BeautifulSoup

# def parse_branches(html):
#     soup = BeautifulSoup(html, 'html.parser')
#     branches = []

#     for branch in soup.select(".branch-card"):
#         name = branch.select_one(".card-title").text.strip()
#         hours = branch.select(".card-text")[0].get_text(" ", strip=True)
#         phone_info = branch.select(".card-text")[1].get_text(" ", strip=True) if len(branch.select(".card-text")) > 1 else ""
#         location = branch.select(".card-text")[-1].get_text(" ", strip=True)

#         branches.append({
#             "name": name,
#             "hours": hours,
#             "phone_info": phone_info,
#             "location": location
#         })

#     return branches

# def write_to_md(branches, filename="branches.md"):
#     with open(filename, "w", encoding="utf-8") as f:
#         f.write("# Салбрын жагсаалт\n")
#         for branch in branches:
#             f.write(f"## {branch['name']}\n")
#             f.write(f"**Ажиллах цаг:** {branch['hours']}\n")
#             f.write(f"**холбоо барих:** {branch['phone_info']}\n")
#             f.write(f"**Хаяг:** {branch['location']}\n")

# # Example usage
# # html = """(your HTML content here)"""
# branches = parse_branches(html)
# write_to_md(branches)
