; AI Bot Professional Windows Installer
; Built with InnoSetup (https://jrsoftware.org/iszdown.php)
; This creates a professional installation package

[Setup]
AppName=AI Bot
AppVersion=1.0
AppPublisher=AI Bot Project
AppPublisherURL=https://github.com/yourusername/ai-bot-github
AppSupportURL=https://github.com/yourusername/ai-bot-github/issues
AppUpdatesURL=https://github.com/yourusername/ai-bot-github
DefaultDirName={autopf}\AI Bot
DefaultGroupName=AI Bot
AllowNoIcons=yes
LicenseFile=LICENSE
SetupIconFile=ai_bot\gui\icon.ico
UninstallIconFile=ai_bot\gui\icon.ico
OutputDir=.\dist
OutputBaseFilename=AI_Bot_Setup
Compression=lzma
SolidCompression=yes
WizardStyle=modern
PrivilegesRequired=lowest

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "spanish"; MessagesFile: "compiler:Languages\Spanish.isl"
Name: "french"; MessagesFile: "compiler:Languages\French.isl"
Name: "german"; MessagesFile: "compiler:Languages\German.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked
Name: "quicklaunchicon"; Description: "{cm:CreateQuickLaunchIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked; OnlyBelowVersion: 0,6.1

[Files]
Source: "dist\AIBot.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "ai_bot\*"; DestDir: "{app}\ai_bot"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "requirements.txt"; DestDir: "{app}"; Flags: ignoreversion
Source: "config.json"; DestDir: "{app}"; Flags: ignoreversion
Source: "README.md"; DestDir: "{app}"; Flags: ignoreversion
Source: "LICENSE"; DestDir: "{app}"; Flags: ignoreversion
Source: "wiki_dumps.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "wiki_to_sqlite.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "uninstall.bat"; DestDir: "{app}"; Flags: ignoreversion
Source: "uninstall.py"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\AI Bot"; Filename: "{app}\AIBot.exe"; IconFilename: "{app}\ai_bot\gui\icon.ico"
Name: "{group}\{cm:UninstallProgram,AI Bot}"; Filename: "{uninstallexe}"
Name: "{autodesktop}\AI Bot"; Filename: "{app}\AIBot.exe"; IconFilename: "{app}\ai_bot\gui\icon.ico"; Tasks: desktopicon
Name: "{userappdata}\Microsoft\Internet Explorer\Quick Launch\AI Bot"; Filename: "{app}\AIBot.exe"; IconFilename: "{app}\ai_bot\gui\icon.ico"; Tasks: quicklaunchicon

[Run]
Filename: "{app}\AIBot.exe"; Description: "{cm:LaunchProgram,AI Bot}"; Flags: nowait postinstall skipifsilent

[InstallDelete]
Type: filesandordirs; Name: "{app}\*"

[Code]
procedure InitializeWizard;
begin
  WizardForm.WelcomeLabel1.Caption := 'Welcome to AI Bot Setup';
  WizardForm.WelcomeLabel2.Caption := 
    'This wizard will guide you through the installation of AI Bot, ' +
    'a professional hybrid search engine with online and offline capabilities.' + #13 + #13 +
    'AI Bot will:' + #13 +
    '  • Search the internet in real-time' + #13 +
    '  • Access offline Wikipedia data' + #13 +
    '  • Securely store your search history' + #13 +
    '  • Run entirely locally on your machine';
end;

procedure CurStepChanged(CurStep: TSetupStep);
begin
  if CurStep = ssInstall then
    MsgBox('Installation is starting. Your system will be configured with all necessary components.', mbInformation, MB_OK);
end;
