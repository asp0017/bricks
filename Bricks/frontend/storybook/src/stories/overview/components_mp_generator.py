# change "components map.mdx" to "components map.md"

import os

mdx = open("Bricks/frontend/storybook/src/stories/overview/components_map.mdx", "r").readlines()
md = open("Bricks/frontend/storybook/src/stories/overview/components_map.md", "w")

dismiss_lines = range(1,20)
not_translate_lines = [ 26 ]

md.write("> 📌 Updated: " + os.popen("date").read())
def translater(mdx:str)->str:
    md = mdx.replace("- ", "\n- ❌ ")
    md = md.replace("❌ **", "🖥️ **")
    md = md.replace("❌ *", "📌 *")
    md = md.replace("❌ ***", "🎨 ***")
    return md

for i in range(len(mdx)):
    if i+1 in dismiss_lines:
        continue
    if i+1 in not_translate_lines:
        md.write(mdx[i])
        continue
    md.write(translater(mdx[i]))
    





