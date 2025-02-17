folder('Tools') {
  displayName('Tools')
  description('Folder for miscellaneous tools.')

  freeStyleJob('Tools/clone-repository') {
    description('Clone a Git repository.')
    parameters {
      stringParam('GIT_REPOSITORY_URL', '', 'Git URL of the repository to clone')
    }
    steps {
      shell('git clone $GIT_REPOSITORY_URL')
    }
    wrappers {
      preBuildCleanup()
    }
  }

  freeStyleJob('/Tools/SEED') {
    description('SEED job to create jobs based on parameters.')
    parameters {
      stringParam('GITHUB_NAME', '', 'GitHub repository owner/repo_name (e.g.: "EpitechIT31000/chocolatine")')
      stringParam('DISPLAY_NAME', '', 'Display name for the job')
    }
    steps {
      dsl {
        text('''
          job("$DISPLAY_NAME") {
            triggers {
              scm('* * * * *')
            }
            scm {
              github("$GITHUB_NAME")
            }
            steps {
              shell('make fclean')
              shell('make')
              shell('make tests_run')
              shell('make clean')
            }
            wrappers {
              preBuildCleanup()
            } 
          }
          '''.stripIndent()
        )
      }
    }
  }
}

// freeStyleJob('Tools/SEED') {
//   description('SEED job to create jobs based on parameters.')
//   parameters {
//     stringParam('GITHUB_NAME', '', 'GitHub repository owner/repo_name (e.g.: "EpitechIT31000/chocolatine")')
//     stringParam('DISPLAY_NAME', '', 'Display name for the job')
//   }
//   scm {
//     git {
//       remote {
//         url('https://github.com/$GITHUB_NAME')
//       }
//     }
//   }
//   steps {
//     jobDsl {
//       targets('job_dsl.groovy')
//     }
//   }
// }

// job("${DISPLAY_NAME}") {
//     description("Job generated for ${GITHUB_NAME}")
//     properties {
//         githubProjectUrl("https://github.com/${GITHUB_NAME}")
//     }
//     scm {
//         git {
//             remote {
//                 url("https://github.com/${GITHUB_NAME}.git")
//             }
//         }
//     }
//     triggers {
//         scm('* * * * *')
//     }
//     wrappers {
//         preBuildCleanup()
//     }
//     steps {
//         shell('make fclean')
//         shell('make')
//         shell('make tests_run')
//         shell('make clean')
//     }
// }
