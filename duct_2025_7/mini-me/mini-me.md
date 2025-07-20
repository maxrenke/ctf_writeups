# CTF Writeup: DUCTF Client-Side Hacking Challenge

## Challenge Overview
- **Target**: `https://web-mini-me-ab6d19a7ea6e.2025-us.ductf.net/`
- **Goal**: Find the API key to access `/admin/flag` endpoint
- **Flag**: `DUCTF{Cl13nt-S1d3-H4ck1nG-1s-FuN}`

## Step-by-Step Solution

### Step 1: Initial Reconnaissance
Visited the target URL and found a simple login page with the title "EmailCTF Webmail".

### Step 2: View Page Source
Examined the HTML source code:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>EmailCTF Login</title>
    <link rel="stylesheet" href="/static/css/style.css" />
</head>
<body>
    <div class="login-container">
        <h1>EmailCTF Webmail</h1>
        <form method="POST" action="/login">
            <input type="text" placeholder="Email" required />
            <input type="password" placeholder="Password" required />
            <button type="submit">Login</button>
        </form>
    </div>
    <script src="/static/js/main.min.js"></script>
</body>
</html>
```

### Step 3: Examine JavaScript File
Accessed `/static/js/main.min.js` and found minified JavaScript code with a crucial comment at the end:
```javascript
//test map file -> test-main.min.js.map, remove in prod
```

### Step 4: Access Source Map File
The comment revealed a source map file that should have been removed in production. Accessed:
`/static/js/test-main.min.js.map`

### Step 5: Analyze Source Map
Found an obfuscated function `qyrbkc()` containing arrays of numbers:
```javascript
function qyrbkc() { 
    const xtqzp = ["85"], vmsdj = ["87"], rlfka = ["77"], wfthn = ["67"], zdqo = ["40"], yclur = ["82"],
          bpxmg = ["82"], hkfav = ["70"], oqzdu = ["78"], nwtjb = ["39"], sgfyk = ["95"], utxzr = ["89"],
          jvmqa = ["67"], dpwls = ["73"], xaogc = ["34"], eqhvt = ["68"], mfzoj = ["68"], lbknc = ["92"],
          zpeds = ["84"], cvnuy = ["57"], ktwfa = ["70"], xdglo = ["87"], fjyhr = ["95"], vtuze = ["77"], awphs = ["75"];
    
    const dhgyvu = [xtqzp[0], vmsdj[0], rlfka[0], wfthn[0], zdqo[0], yclur[0], 
                    bpxmg[0], hkfav[0], oqzdu[0], nwtjb[0], sgfyk[0], utxzr[0], 
                    jvmqa[0], dpwls[0], xaogc[0], eqhvt[0], mfzoj[0], lbknc[0], 
                    zpeds[0], cvnuy[0], ktwfa[0], xdglo[0], fjyhr[0], vtuze[0], awphs[0]];

    const lmsvdt = dhgyvu.map((pjgrx, fkhzu) =>
        String.fromCharCode(
            Number(pjgrx) ^ (fkhzu + 1) ^ 0 
        )
    ).reduce((qdmfo, lxzhs) => qdmfo + lxzhs, ""); 
    console.log("Note: Key is now secured with heavy obfuscation, should be safe to use in prod :)");
}
```

### Step 6: Decode the API Key
The function XORs each number with its position (index + 1). Created a decoder:
```javascript
const numbers = [85, 87, 77, 67, 40, 82, 82, 70, 78, 39, 95, 89, 67, 73, 34, 68, 68, 92, 84, 57, 70, 87, 95, 77, 75];
const result = numbers.map((num, index) => String.fromCharCode(num ^ (index + 1))).join('');
console.log(result); // Output: TUNG-TUNG-TUNG-TUNG-SAHUR
```

### Step 7: Get the Flag
Used the decoded API key to access the flag endpoint:
```bash
curl -X POST -H "X-API-Key: TUNG-TUNG-TUNG-TUNG-SAHUR" https://web-mini-me-ab6d19a7ea6e.2025-us.ductf.net/admin/flag
```

**Result**: `DUCTF{Cl13nt-S1d3-H4ck1nG-1s-FuN}`

## Key Takeaways
1. **Source maps are dangerous** - Never leave `.map` files in production
2. **Client-side obfuscation is not security** - Anything on the client can be reverse-engineered
3. **Always check static files** - Look for forgotten development artifacts
4. **Comments matter** - Developer comments often reveal important information