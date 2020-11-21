'use babel';

import MySecondPackageView from './my-second-package-view';
import { CompositeDisposable } from 'atom';
var Promise = require('promise');

export default {

    mySecondPackageView: null,
    modalPanel: null,
    subscriptions: null,

    activate(state) {
        this.mySecondPackageView = new MySecondPackageView(state.mySecondPackageViewState);
        this.modalPanel = atom.workspace.addModalPanel({
            item: this.mySecondPackageView.getElement(),
            visible: false
        });
        // Events subscribed to in atom's system can be easily cleaned up with a CompositeDisposable
        this.subscriptions = new CompositeDisposable();

        // Register command that toggles this view
        atom.workspace.activePaneContainer.paneContainer.element.addEventListener("dblclick", this.toggle());
        this.subscriptions.add(atom.commands.add('atom-workspace', {
            'my-second-package:toggle': () => this.toggle()
        }));
    },

    deactivate() {
        console.log("Deactivate");
        this.modalPanel.destroy();
        this.subscriptions.dispose();
        this.mySecondPackageView.destroy();

    },

    serialize() {
        return {
            mySecondPackageViewState: this.mySecondPackageView.serialize()
        };
    },

    toggle() {
        mySecondPackageView = this.mySecondPackageView;
        modalPanel = this.modalPanel;
        tmp = "123";
        final_array = 0;
        console.log('MySecondPackage was toggled!');
        if (this.modalPanel.isVisible()) {
            console.log("entered if");
            this.mySecondPackageView.empty_array();
            this.modalPanel.hide();
            this.deactivate();
        }
        console.log("Activate");
        const editor = atom.workspace.getActiveTextEditor();
        console.log(editor);
        console.log(editor.getSelectedText());
        var completeCode = editor.getText();
        const fs = require('fs');
        const path = require('path');
        const p = path.join(__dirname, '..', 'node_modules', 'node-powershell')
        const shell = require(p);

        var injectCode_python;
        const injectionCode_python_path = path.join(__dirname, 'injectCodepython.txt');
        var read_python_path = path.join(__dirname, 'read_python.txt');
        var webpage = path.join(__dirname, 'html_new1.html');
        read_python_path = read_python_path.replace(/\\/gi, "\\\\");
        console.log(injectionCode_python_path);

        var injectCode_python = fs.readFileSync(injectionCode_python_path);
        combining_code(injectCode_python, step1);
        console.log("call has ended");
        var final_array;
        function step1() {
            run_powershell(step2);
            console.log("exit step1");
        }
        function step2() {
            console.log("enter step2");
            get_array();
        }
        function step3() {
            run_functions()
        }



        function combining_code(injectCode_python, callback) {
            injectCode_python = new TextDecoder("utf-8").decode(injectCode_python);

            injectCode_python = injectCode_python.replace(/<__b__s__>/gi, completeCode);
            const fname = path.join(__dirname, 'python_output.py');
            let data = injectCode_python;
            fs.writeFileSync(fname, data, 'utf-8');
            console.log("write file completed");
            callback();

        }

        function run_powershell(callback) {

            console.log("powershell started");
            let ps = new shell({
                executionPolicy: 'Bypass',
                noProfile: true
            });

            ps.addCommand('cd ' + __dirname)
            ps.invoke()
                .then(output => {
                    console.log("hello");
                    let ps1 = new shell({
                        executionPolicy: 'Bypass',
                        noProfile: true
                    });
                    ps.addCommand('py python_output.py')
                    ps.invoke()
                        .then(output => {
                            callback();
                        })
                        .catch(err => {
                            console.log(err)
                        })
                    console.log(output)
                })
                .catch(err => {
                    console.log(err);
                });
            console.log("powershell has ended");

        }

        function get_array() {
            window.open(webpage)
            console.log("end")
        }


    }

};
