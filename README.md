# vivaldi-restore-urls

<h3>Tool for exporting URLs from Vivaldi session files</h3>

Sometimes when Vivaldi crashes and you re-open it, it won't be able to restore your previous session (or not completely; for example, some Workplaces might be missing).

This can be very frustrating, but if this happens, you might still be able to recover the URLs of the tabs you had open.

There are three files included in this utility:

<ul>
    <li><code>export_urls.py</code>: Finds URLs in a Vivaldi session file and exports them into a text file.</li>
    <li><code>merge_output.py</code>: Merges exported files into one file as they can contain duplicates.</li>
    <li><code>open_urls.py</code>: Opens all URLs in the export file.</li>
</ul>

<h1>How to use</h1>

As soon as you reopened Vivaldi and discovered that it had failed to restore your session, don't click anything else in Vivaldi, as it could rewrite your old session files any moment, rendering them unrecoverable.

<ul>
    <li>If you want to be sure that they won't be overwritten, you should create a copy of the files every time Vivaldi crashes, before re-opening it.</li>
</ul>

Make a copy of all your <code>Session</code> and <code>Tabs</code> files found at the following location:

<ul>
    <li><b>Linux (Ubuntu)</b>: <code>/home/[username]/.config/vivaldi/Default/Sessions/</code></li>
    <li><b>Windows:</b> <code>C:\Users\[username]\AppData\Local\Vivaldi\User Data\Default\Sessions\</code></li>
</ul>

These files likely also include some URLs for tabs that you had already closed; it won't be an exact match of your open tabs before the crash. And some URLs for tabs that were open might still be missing from these files. But still, it's better to restore some wanted and some unwanted tabs than none at all.

Make a UTF-8 copy of these files and move them directly into the directory of this tool (next to the Python files).

<ul>
    <li>You can use your basic text editor such as Kate or Notepad to do this.</li>
</ul>

Now, using Python (<a href="https://www.python.org/downloads/">install</a> it if you don't yet have it), run export_urls.py supplying the file name to be processed as argument (one at a time) (the original files will remain intact).

<ul>
    <li>For example:</li>
    <ul>
        <li><code>python3 export_urls.py Session_13338542211042924</code></li>
        <li>In Bash (Linux), you would use <code>python3</code>.</li>
        <li>In Command Prompt / PowerShell (Windows) you would use simply <code>python</code>.</li>
    </ul>
</ul>

Your output files will be placed in the <code>dist</code> folder within the main directory of this tool.

If you exported several files, they will often contain many duplicates. You can run <code>merge_output.py</code> (no arguments required) in order to merge them into a single file (the original files will remain intact). The merged file will also be placed in the <code>dist</code> directory.

Finally, if you don't wish to open the URLs manually, you can run <code>open_urls.py</code>, which can automatically open all URL in a chosen export (or merged export) file. You need to supply a file path and a time delay (in seconds) as arguments.

<ul>
    <li>The time delay specifies the delay between two calls for opening URLs. If there were no delay between the calls, your browser (or computer) would likely crash when trying to open a large number of tabs all at once.</li>
    <ul>
        <li>5 seconds worked fine on my computer with 250 tabs, but if you computer is slower or your have even more URLs, you might be safer setting it at 10 or 15 seconds.</li>
    </ul>
    <li>For example:</li>
    <ul>
        <li><code>python3 open_urls.py ./dist/merged-1694191015.2006676.txt 5</code></li>
    </ul>
</ul>
