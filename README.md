# Muse_2

A fresh Kivy/Buildozer Android project with a small functional menu app and a GitHub Actions workflow that builds a debug APK.

## Important build choice

This project uses **Android min API 24 (Android 7.0+)**. The reported Muse_1 compiler error came from compiling Python 3.14 against Android API 23: `preadv` and `pwritev` are only available from API 24 on Android. The workflow checks that `android.minapi = 24` remains set.

## Files

- `main.py` — functional starter menu (save note, copy text, open website, about, clear).
- `buildozer.spec` — Android package and build settings.
- `.github/workflows/android.yml` — builds the debug APK on pushes to `main` or `master`, and manually from Actions.

## Build on GitHub

1. Create a **new, empty repository named `Muse_2`**.
2. Upload the contents of this ZIP to the repository root (including the `.github` folder).
3. Commit to `main` or `master`.
4. Open **Actions → Build Muse_2 Android APK**.
5. When the run succeeds, download the artifact named `Muse_2-Android-APK`.

The ZIP contains project source and workflow, not a prebuilt APK. GitHub Actions must complete successfully to produce the APK. A cloud build can still reveal other dependency or runner issues; the API 24 change specifically addresses the compiler error shown in the Muse_1 log.
