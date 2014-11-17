import FWCore.ParameterSet.Config as cms

import HeavyIonsAnalysis.HiTrkEffAnalyzer.hitrackingParticleSelector_cfi

cutsTPForFak = HeavyIonsAnalysis.HiTrkEffAnalyzer.hitrackingParticleSelector_cfi.hitrackingParticleSelector.clone()
cutsTPForEff = cutsTPForFak.clone(primaryOnly = cms.bool(True))

# Higher pt threshold
cutsTPForFakHigh = HeavyIonsAnalysis.HiTrkEffAnalyzer.hitrackingParticleSelector_cfi.hitrackingParticleSelector.clone(ptMin = cms.double(4.0))

cutsTPForFakPxl = HeavyIonsAnalysis.HiTrkEffAnalyzer.hitrackingParticleSelector_cfi.hitrackingParticleSelector.clone(ptMin = cms.double(0.1))
cutsTPForEffPxl = cutsTPForFakPxl.clone(primaryOnly = cms.bool(True))
