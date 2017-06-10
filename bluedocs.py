# -*- coding: utf-8 -*-
"""
    BlueDocs (A MoinMoin theme)
    @copyright: 2014 WATANABE Takuma <takumaw@sfo.kuramae.ne.jp>
"""

from MoinMoin import wikiutil
from MoinMoin.theme import ThemeBase
from MoinMoin.Page import Page

class Theme(ThemeBase):

    name = 'bluedocs'

    _ = lambda x: x
    icons = {
        # key          alt                        icon filename      w   h
        # ------------------------------------------------------------------
        # navibar
        'help':        ("%(page_help_contents)s", "moin-help.png",   15, 15),
        'find':        ("%(page_find_page)s",     "moin-search.png", 15, 15),
        'diff':        (_("Diffs"),               "moin-diff.png",   15, 15),
        'info':        (_("Info"),                "moin-info.png",   15, 15),
        'edit':        (_("Edit"),                "moin-edit.png",   15, 15),
        'unsubscribe': (_("Unsubscribe"),         "moin-unsubscribe.png", 15, 15),
        'subscribe':   (_("Subscribe"),           "moin-subscribe.png",   15, 15),
        'raw':         (_("Raw"),                 "moin-raw.png",    15, 15),
        'xml':         (_("XML"),                 "moin-xml.png",    36, 14),
        'print':       (_("Print"),               "moin-print.png",  15, 15),
        'view':        (_("View"),                "moin-show.png",   15, 15),
        'home':        (_("Home"),                "moin-home.png",   15, 15),
        'up':          (_("Up"),                  "moin-parent.png", 15, 13),
        # FileAttach
        'attach':     ("%(attach_count)s",       "moin-attach.png",  15, 15),
        'attachimg':  ("",                       "attach.png",       15, 15),
        # RecentChanges
        'rss':        (_("[RSS]"),               "moin-rss.png",     15, 15),
        'deleted':    (_("[DELETED]"),           "moin-deleted.png", 15, 15),
        'updated':    (_("[UPDATED]"),           "moin-updated.png", 15, 15),
        'renamed':    (_("[RENAMED]"),           "moin-renamed.png", 15, 15),
        'conflict':   (_("[CONFLICT]"),          "moin-conflict.png",15, 15),
        'new':        (_("[NEW]"),               "moin-new.png",     15, 15),
        'diffrc':     (_("[DIFF]"),              "moin-diff.png",    15, 15),
        # General
        'bottom':     (_("[BOTTOM]"),            "moin-bottom.png", 15, 15),
        'top':        (_("[TOP]"),               "moin-top.png",    15, 15),
        'www':        ("[WWW]",                  "moin-www.png",    15, 15),
        'mailto':     ("[MAILTO]",               "moin-email.png",  15, 15),
        'news':       ("[NEWS]",                 "moin-news.png",   15, 15),
        'telnet':     ("[TELNET]",               "moin-telnet.png", 15, 15),
        'ftp':        ("[FTP]",                  "moin-ftp.png",    15, 15),
        'file':       ("[FILE]",                 "moin-ftp.png",    15, 15),
        # search forms
        'searchbutton': ("[?]",                  "moin-search.png", 15, 15),
        'interwiki':  ("[%(wikitag)s]",          "moin-inter.png",  15, 15),

        # smileys (this is CONTENT, but good looking smileys depend on looking
        # adapted to the theme background color and theme style in general)
        #vvv    ==      vvv  this must be the same for GUI editor converter
        'X-(':        ("X-(",                    'angry.png',       15, 15),
        ':D':         (":D",                     'biggrin.png',     15, 15),
        '<:(':        ("<:(",                    'frown.png',       15, 15),
        ':o':         (":o",                     'redface.png',     15, 15),
        ':(':         (":(",                     'sad.png',         15, 15),
        ':)':         (":)",                     'smile.png',       15, 15),
        'B)':         ("B)",                     'smile2.png',      15, 15),
        ':))':        (":))",                    'smile3.png',      15, 15),
        ';)':         (";)",                     'smile4.png',      15, 15),
        '/!\\':       ("/!\\",                   'alert.png',       15, 15),
        '<!>':        ("<!>",                    'attention.png',   15, 15),
        '(!)':        ("(!)",                    'idea.png',        15, 15),

        # copied 2001-11-16 from http://pikie.darktech.org/cgi/pikie.py?EmotIcon
        ':-?':        (":-?",                    'tongue.png',      15, 15),
        ':\\':        (":\\",                    'ohwell.png',      15, 15),
        '>:>':        (">:>",                    'devil.png',       15, 15),
        '|)':         ("|)",                     'tired.png',       15, 15),

        # some folks use noses in their emoticons
        ':-(':        (":-(",                    'sad.png',         15, 15),
        ':-)':        (":-)",                    'smile.png',       15, 15),
        'B-)':        ("B-)",                    'smile2.png',      15, 15),
        ':-))':       (":-))",                   'smile3.png',      15, 15),
        ';-)':        (";-)",                    'smile4.png',      15, 15),
        '|-)':        ("|-)",                    'tired.png',       15, 15),

        # version 1.0
        '(./)':       ("(./)",                   'checkmark.png',   15, 15),
        '{OK}':       ("{OK}",                   'thumbs-up.png',   15, 15),
        '{X}':        ("{X}",                    'icon-error.png',  15, 15),
        '{i}':        ("{i}",                    'icon-info.png',   15, 15),
        '{1}':        ("{1}",                    'prio1.png',       15, 15),
        '{2}':        ("{2}",                    'prio2.png',       15, 15),
        '{3}':        ("{3}",                    'prio3.png',       15, 15),

        # version 1.3.4 (stars)
        # try {*}{*}{o}
        '{*}':        ("{*}",                    'star_on.png',     15, 15),
        '{o}':        ("{o}",                    'star_off.png',    15, 15),

        # misc
        'up':              ("[UP]",              "moin-up.png",         15, 15),
        'parent':          ("[PARENT]",          "moin-parent.png",     15, 15),
        'xml2':            (_("XML"),            "moin-xml2.png",       36, 14),
        'moin-icon':       ("MoinMoin",          "moin-icon.png",       15, 15),
        'admon-caution':   ("Caution",           "admon-caution.png",   15, 15),
        'admon-important': ("Important",         "admon-important.png", 15, 15),
        'admon-note':      ("Note",              "admon-note.png",      15, 15),
        'admon-tip':       ("Tip",               "admon-tip.png",       15, 15),
        'admon-warning':   ("Warning",           "admon-warning.png",   15, 15),
    }
    del _

    def header(self, d, **kw):
        """
        Assemble page header

        @param d: parameter dictionary
        @rtype: string
        @return: page header html
        """
        request = self.request
        _ = request.getText
        html = [
            # Pre header custom html
            self.emit_custom_html(self.cfg.page_header1),

            # Header
            u'<div id="header">',
            self.logo(),
            u'<div id="search">',
            self.searchform(d),
            u'</div>',
            u'</div>',

            # Sidebar
            u'<div id="sidebar">',
            u'<p class="section">' + _('Contents') + u'</p>',
            self.navibar(d),
            u'<p class="section">' + _('User') + u'</p>',
            self.username(d),
        ]
        if request.user.valid and request.user.name:
            html += [
                u'<p class="section">' + _('Edit') + u'</p>',
                self.editbar(d),
            ]
        html += [
            u'</div>',

            # Message
            self.msg(d),

            # Location
            u'<div id="location">',
            self.interwiki(d),
            self.title_with_separators(d),
            self.trail(d),
            u'</div>',

            # Post header custom html (not recommended)
            self.emit_custom_html(self.cfg.page_header2),

            # Start of page
            self.startPage(),
        ]
        return u'\n'.join(html)

    editorheader = header

    def footer(self, d, **keywords):
        """
        Assemble wiki footer

        @param d: parameter dictionary
        @keyword ...:...
        @rtype: unicode
        @return: page footer html
        """
        request = self.request
        page = d['page']
        html = [
            # Page into
            self.pageinfo(page),

            # End of page
            self.endPage(),

            # Pre footer custom html (not recommended)
            self.emit_custom_html(self.cfg.page_footer1),

            # Footer
            u'<div id="footer">',
            self.credits(d),
            u'</div>',

            # Post footer custom html
            self.emit_custom_html(self.cfg.page_footer2),
        ]
        return u'\n'.join(html)

    def searchform(self, d):
        """
        assemble HTML code for the search forms

        @param d: parameter dictionary
        @rtype: unicode
        @return: search form html
        """
        _ = self.request.getText
        form = self.request.values
        updates = {
            'search_label': _('Search:'),
            'search_label_wo_colon': _('Search'),
            'search_value': wikiutil.escape(form.get('value', ''), 1),
            'search_full_label': _('Text'),
            'search_title_label': _('Titles'),
            'url': self.request.href(d['page'].page_name)
            }
        d.update(updates)

        html = u'''
<form id="searchform" method="get" action="%(url)s">
<div>
<input type="hidden" name="action" value="fullsearch">
<input type="hidden" name="context" value="180">
<label for="searchinput">%(search_label)s</label>
<input id="searchinput" type="text" name="value" value="%(search_value)s" size="20"
    onfocus="searchFocus(this)" onblur="searchBlur(this)"
    onkeyup="searchChange(this)" onchange="searchChange(this)" alt="Search">
<input input id="fullsearch" name="fullsearch" type="submit"
    value="%(search_label_wo_colon)s" alt="Search Full Text">
<!--input id="fullsearch" name="fullsearch" type="submit"
    value="%(search_full_label)s" alt="Search Full Text">
<input id="titlesearch" name="titlesearch" type="submit"
    value="%(search_title_label)s" alt="Search Titles"-->
</div>
</form>
<script type="text/javascript">
<!--// Initialize search form
var f = document.getElementById('searchform');
f.getElementsByTagName('label')[0].style.display = 'none';
var e = document.getElementById('searchinput');
searchChange(e);
searchBlur(e);
//-->
</script>
''' % d
        return html
