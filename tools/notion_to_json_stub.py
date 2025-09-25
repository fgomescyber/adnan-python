# Stub to convert Markdown lessons into a canonical JSON bundle
import sys, glob, os, json
def convert(input_dir, out_file):
    lessons = []
    for md in glob.glob(os.path.join(input_dir, '*.md')):
        with open(md, 'r', encoding='utf-8') as f:
            lessons.append({'file': os.path.basename(md), 'content': f.read()})
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump({'lessons': lessons}, f, indent=2, ensure_ascii=False)
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('usage: notion_to_json_stub.py <input_dir> <output.json>')
    else:
        convert(sys.argv[1], sys.argv[2])
