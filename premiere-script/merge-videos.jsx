var project = app.project;
var outputFilePath = "~/Documents/history-queefs/history-queefs/premiere-script";
var filesFolderPath = "~/Documents/history-queefs/history-queefs/premiere-script/input-vids";

// import video files into project
var filesFolder = new Folder(filesFolderPath);
var files = filesFolder.getFiles("*.mp4");
var filePaths = [];
for (var i = 0; i < files.length; i++) {
    var filePath = addExtraBackslash(files[i].fsName);
    filePaths.push(filePath);
}
var importSuccess = project.importFiles(filePaths);

// insert clips into sequence
var availableClipsCollection = project.rootItem.children;
var availableClipsArray = [];
for (var i = 0; i < availableClipsCollection.length; i++) {
    availableClipsArray.push(availableClipsCollection[i])
}
var firstSeq = project.createNewSequenceFromClips("sequence 1", availableClipsArray, null);

// // Export the sequence as an MP4 file
// var exportSettings = app.encoder.createExportOptions(outputFilePath, 1080, 1920, app.encoder.ENCODE_QUALITY_HIGH);
// exportSettings.setPresetFormat("MP4");
// app.encoder.exportSequence(seq, outputFilePath, exportSettings);

function addExtraBackslash(str) {
    return str.replace(/\\/g, "\\\\");
}