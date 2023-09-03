### Challenge: xxd-server

#### Category: web

#### Description: I wrote a little app that allows you to hex dump files over the internet.

#### Author: hashkitten

The first thing I did was analyze the source code. The Dockerfile provided shows that the flag is in the root directory with the file name as "flag" and that the server seems to run an Apache service (as implied from the configuration files). In index.php, it seems that you can upload files to the website provided, and it will store its contents as the output of the xxd command in the server with the filename that you sent it intact:

```php
// Is there an upload?
if (isset($_FILES['file-upload'])) {
        $upload_dir = 'uploads/' . bin2hex(random_bytes(8));
        $upload_path = $upload_dir . '/' . basename($_FILES['file-upload']['name']);
        mkdir($upload_dir);
        $upload_contents = xxd(file_get_contents($_FILES['file-upload']['tmp_name']));
        if (file_put_contents($upload_path, $upload_contents)) {
                $message = 'Your file has been uploaded. Click <a href="' . htmlspecialchars($upload_path) . '">here</a> to view';
        } else {
            $message = 'File upload failed.';
        }
}
```

The file of most importance is the .htaccess file:

```
# Everything not a PHP file, should be served as text/plain
<FilesMatch "\.(?!(php)$)([^.]*)$">
    ForceType text/plain
</FilesMatch>
```

Here, the server takes in all files that aren't PHP files and interprets them as text files. However, *any PHP files uploaded to the server will be interpreted as PHP files*. Thus, the bug is made clear: if you upload a PHP file, the contents inside will be taken in and interpreted as code. However the ```xxd()``` function in the index.php file will modify the contents of the PHP file when it is uploaded, so I had to craft the payload in the file so as to comment out the xxd-like output generated. With that, I created a payload that used the ```require``` PHP command to read off the flag from its location on the web server.

#### Flag: DUCTF{00000000__7368_656c_6c64_5f77_6974_685f_7878_6421__shelld_with_xxd!}

Solved by giggsterpuku
