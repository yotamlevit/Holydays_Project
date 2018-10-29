#############################################################################
# Generated by PAGE version 4.18
#  in conjunction with Tcl version 8.6
#  Oct 29, 2018 11:08:07 AM +0200  platform: Windows NT
set vTcl(timestamp) ""


if {!$vTcl(borrow)} {

set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #d9d9d9
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #d8d8d8
set vTcl(active_menu_fg) #000000
}

#############################################################################
#################################
#LIBRARY PROCEDURES
#


if {[info exists vTcl(sourcing)]} {

proc vTcl:project:info {} {
    set base .top42
    global vTcl
    set base $vTcl(btop)
    if {$base == ""} {
        set base .top42
    }
    namespace eval ::widgets::$base {
        set dflt,origin 0
        set runvisible 1
    }
    namespace eval ::widgets_bindings {
        set tagslist _TopLevel
    }
    namespace eval ::vTcl::modules::main {
        set procs {
        }
        set compounds {
        }
        set projectType single
    }
}
}

#################################
# GENERATED GUI PROCEDURES
#

proc vTclWindow.top42 {base} {
    if {$base == ""} {
        set base .top42
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu "$top.m43" -background {#d9d9d9} -highlightbackground {#d9d9d9} \
        -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 311x183+559+180
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1924 1061
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "Creat Right Teiangle"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    set site_3_0 $top.m43
    menu $site_3_0 \
        -activebackground {#d8d8d8} -activeforeground {#000000} \
        -background {#d9d9d9} -font font9 -foreground {#000000} -tearoff 0 
    entry $top.ent45 \
        -background white -disabledforeground {#a3a3a3} -font font10 \
        -foreground {#000000} -insertbackground black 
    vTcl:DefineAlias "$top.ent45" "side_one" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab46 \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -foreground {#000000} -text {Side One - } -width 62 
    label $top.lab47 \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -foreground {#000000} -text {Side Two -} 
    vTcl:DefineAlias "$top.lab47" "Label2" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent48 \
        -background white -disabledforeground {#a3a3a3} -font font10 \
        -foreground {#000000} -insertbackground black 
    vTcl:DefineAlias "$top.ent48" "side_two" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent49 \
        -background white -disabledforeground {#a3a3a3} -font font10 \
        -foreground {#000000} -insertbackground black 
    vTcl:DefineAlias "$top.ent49" "x_start" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab50 \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -foreground {#000000} -text {Start Point (x)} 
    vTcl:DefineAlias "$top.lab50" "Label3" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab51 \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -foreground {#000000} -text {Creat Right Triangle} 
    vTcl:DefineAlias "$top.lab51" "Label4" vTcl:WidgetProc "Toplevel1" 1
    button $top.but53 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -pady 0 -text Creat 
    vTcl:DefineAlias "$top.but53" "Creat" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab54 \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -foreground {#000000} -text {Start Point (y)} 
    vTcl:DefineAlias "$top.lab54" "Label5" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent55 \
        -background white -disabledforeground {#a3a3a3} -font font10 \
        -foreground {#000000} -insertbackground black 
    vTcl:DefineAlias "$top.ent55" "y_start" vTcl:WidgetProc "Toplevel1" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.ent45 \
        -in $top -x 90 -y 50 -width 64 -relwidth 0 -height 20 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab46 \
        -in $top -x 10 -y 50 -width 62 -relwidth 0 -height 31 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab47 \
        -in $top -x 10 -y 80 -anchor nw -bordermode ignore 
    place $top.ent48 \
        -in $top -x 90 -y 80 -width 64 -relwidth 0 -height 20 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.ent49 \
        -in $top -x 90 -y 110 -width 64 -relwidth 0 -height 20 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab50 \
        -in $top -x 10 -y 110 -anchor nw -bordermode ignore 
    place $top.lab51 \
        -in $top -x 10 -y 10 -width 134 -relwidth 0 -height 41 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but53 \
        -in $top -x 160 -y 50 -width 117 -relwidth 0 -height 114 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab54 \
        -in $top -x 10 -y 140 -width 74 -relwidth 0 -height 21 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.ent55 \
        -in $top -x 90 -y 140 -width 64 -relwidth 0 -height 20 -relheight 0 \
        -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

#############################################################################
## Binding tag:  _TopLevel

bind "_TopLevel" <<Create>> {
    if {![info exists _topcount]} {set _topcount 0}; incr _topcount
}
bind "_TopLevel" <<DeleteWindow>> {
    if {[set ::%W::_modal]} {
                vTcl:Toplevel:WidgetProc %W endmodal
            } else {
                destroy %W; if {$_topcount == 0} {exit}
            }
}
bind "_TopLevel" <Destroy> {
    if {[winfo toplevel %W] == "%W"} {incr _topcount -1}
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top42 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}
