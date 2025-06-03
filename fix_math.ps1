$content = Get-Content -Path "draft.md" -Raw

# Fix inline math expressions with single $...$
$content = $content -replace '(?<!\\)\$([^$]+)\$(?!\$)', '$$$1$$'

# Fix display math expressions with $$...$$
$content = $content -replace '\$\$(.*?)\$\$', '$$$$$$$1$$$$$$'

# Fix common LaTeX commands that need escaping
$content = $content -replace '\\\[', '\['
$content = $content -replace '\\\]', '\]'

# Save the fixed content
$content | Out-File -FilePath "draft_fixed.md" -Encoding utf8
